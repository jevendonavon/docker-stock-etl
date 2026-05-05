# Dockerized Stock ETL Pipeline

A containerized ETL pipeline that extracts stock market data, transforms it, 
and loads it into PostgreSQL — packaged with Docker so it runs anywhere.

## What it does

Pulls 6 months of stock data for AAPL, MSFT, GOOGL, and AMZN from Yahoo 
Finance, calculates daily returns and 7-day moving averages, then loads 
the results into a PostgreSQL database.

## Stack

- Docker (containerization)
- Python 3.12
- pandas, yfinance, sqlalchemy, psycopg2

## Files

| File | Description |
|------|-------------|
| `Dockerfile` | Container build instructions |
| `etl.py` | Extract, transform, load script |
| `requirements.txt` | Python dependencies |

## How to run

```bash
docker build -t stock-etl .
docker run --add-host=host.docker.internal:host-gateway stock-etl
```

## What I learned

- How Docker containers work (images, layers, caching)
- Writing a Dockerfile from scratch
- Connecting a Docker container to a host database
- Why containers solve the "works on my machine" problem
