import re  # Dipindahkan ke atas
from fastapi import APIRouter, Query
from playwright.async_api import async_playwright

router = APIRouter()

@router.get("/scrape-mpl")
async def scrape_mpl(data_type: str = Query(..., description="Tipe data: match atau stats")):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        urls = {
            "match": "https://liquipedia.net/mobilelegends/MPL/Indonesia/Season_17/Regular_Season",
            "stats": "https://liquipedia.net/mobilelegends/MPL/Indonesia/Season_17/Statistics"
        }
        
        target_url = urls.get(data_type.lower())
        if not target_url:
            await browser.close()
            return {"error": "Tipe data tidak valid. Gunakan 'match' atau 'stats'."}

        try:
            await page.goto(target_url, wait_until="networkidle", timeout=60000)

            if "Statistics" in target_url:
                rows_data = await page.evaluate('''() => {
                    const rows = Array.from(document.querySelectorAll('.sortable tbody tr'));
                    return rows.map(tr => {
                        const cells = Array.from(tr.querySelectorAll('td, th'));
                        return cells.map(td => td.innerText.trim());
                    });
                }''')

                stats_data = []
                for cells in rows_data:
                    if len(cells) >= 19 and cells[0].isdigit():
                        try:
                            hero_stat = {
                                "type": "hero_stats",
                                "hero_name": cells[1],
                                "pick_count": int(cells[2]),
                                "win_rate": cells[5],
                                "ban_count": int(cells[15]),
                                "presence_rate": cells[18]
                            }
                            stats_data.append(hero_stat)
                        except:
                            continue

                return {
                    "is_direct_json": True,
                    "data_laporan": stats_data
                }
            
            else:
                await page.wait_for_timeout(2000)

                body_text = await page.locator("body").inner_text()

                teams = [
                    "ONIC",
                    "Team Liquid ID",
                    "Dewa United Esports",
                    "Bigetron by Vitality",
                    "EVOS",
                    "Geek Fam ID",
                    "Alter Ego",
                    "Natus Vincere",
                    "RRQ Hoshi"
                ]

                standings_data = []

                for team in teams:
                    pattern = re.compile(
                        rf'(\d+)\.\s+{re.escape(team)}\s+'
                        rf'(?:[▲▼]\s*\d+\s+)?'
                        rf'(\d+-\d+)\s+'
                        rf'(\d+-\d+)\s+'
                        rf'([+-]?\d+)'
                    )

                    match = pattern.search(body_text)

                    if match:
                        standings_data.append({
                            "type": "standings",
                            "rank": int(match.group(1)),
                            "team_name": team,
                            "match_record": match.group(2),
                            "game_record": match.group(3),
                            "game_diff": match.group(4)
                        })

                standings_data.sort(key=lambda x: x["rank"])

                return {
                    "is_direct_json": True,
                    "data_laporan": standings_data,
                }

        except Exception as e:
            return {"error": str(e)}
        finally:
            await browser.close()