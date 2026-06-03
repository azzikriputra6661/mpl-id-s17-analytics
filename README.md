# MPL ID S17 Analytics Platform

Big Data analytics platform for MPL Indonesia Season 17 that integrates data collection, sentiment analysis, dashboard visualization, and WhatsApp chatbot services.

## Overview

This project aims to analyze MPL Indonesia Season 17 data by combining match standings, hero statistics, and audience sentiment from YouTube comments. The processed data is stored in PostgreSQL and visualized through Metabase dashboards. Users can also access analytics information through a WhatsApp chatbot powered by Groq LLM.

## Features

### Dashboard Analytics
- MPL ID S17 Standings
- Team Performance Analysis
- Game Differential Analysis
- Top Picked Heroes
- Top Banned Heroes
- Hero Meta Analysis
- Sentiment Analysis Dashboard

### Sentiment Analysis
- YouTube comment collection
- Automatic sentiment classification
- Category classification
- Team target extraction

### WhatsApp Chatbot
- MPL standings query
- Hero statistics query
- Sentiment information query
- Natural language interaction

## System Architecture

```text
Playwright / YouTube Data API
                │
                ▼
               n8n
                │
                ▼
            Groq LLM
                │
                ▼
           PostgreSQL
           /         \
          ▼           ▼
    Metabase      WAHA API
    Dashboard     WhatsApp Bot
```

## Tech Stack

### Data Collection
- Playwright
- YouTube Data API v3

### Workflow Automation
- n8n

### AI & NLP
- Groq LLM

### Database
- PostgreSQL

### Visualization
- Metabase

### Chatbot
- WAHA (WhatsApp HTTP API)

### Programming Language
- Python

## Dataset

### MPL Standings
- Team rankings
- Match records
- Game records
- Game differential

### Hero Statistics
- Pick count
- Ban count
- Win rate
- Presence rate

### YouTube Comments
- Username
- Comment text
- Sentiment
- Category
- Team target

## Dashboard Components

### Overview
- Total Teams
- Total Heroes
- Total Comments
- Standings Leader

### Team Analytics
- MPL Standings Table
- Game Differential Analysis

### Hero Analytics
- Top Picked Heroes
- Top Banned Heroes
- Pick Count vs Win Rate Analysis

### Sentiment Analytics
- Sentiment Distribution
- Team Target Distribution
- Negative Comment Monitoring

## Chatbot Capabilities

Example queries:

### Standings

```text
User:
klasemen mpl

Bot:
1. ONIC
2. Team Liquid ID
3. Dewa United Esports
...
```

### Hero Statistics

```text
User:
hero paling sering dipick

Bot:
Zhuxin - 107 picks
Claude - 94 picks
...
```

### Sentiment Analysis

```text
User:
sentimen evos

Bot:
Mayoritas komentar terhadap EVOS bersentimen positif...
```

## Limitations

- Sentiment analysis is based on selected MPL Indonesia YouTube videos.
- Team mention distribution depends on the uploaded match videos.
- Results represent the analyzed dataset and may not fully represent all MPL Indonesia audiences.

## Author

Muhammad Azzikri Putra

Department of Computer Engineering  
Institut Teknologi Sepuluh Nopember (ITS)

## Course

Big Data Project
