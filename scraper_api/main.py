from fastapi import FastAPI
from scraper import router as scraper_router

app = FastAPI(
    title="MPL ID S17 - Scraper API",
    description="API untuk mengambil data laporan dari media sosial E100 Suara Surabaya",
    version="1.0.0"
)

app.include_router(scraper_router)