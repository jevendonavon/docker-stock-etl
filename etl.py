import pandas as pd
import yfinance as yf
from sqlalchemy import create_engine
import os

# Config
TICKERS = ['AAPL', 'MSFT', 'GOOGL', 'AMZN']
DB_URL = os.getenv('DATABASE_URL', 'postgresql://postgres:Amgin345@host.docker.internal:5432/stock_etl')

# Extract
print("Extracting stock data...")
df = yf.download(TICKERS, period='6mo', group_by='ticker', auto_adjust=True)
df = df.stack(level=0).reset_index()
df.columns = ['Date', 'ticker', 'Open', 'High', 'Low', 'Close', 'Volume']

# Transform
print("Transforming...")
df['daily_return'] = df.groupby('ticker')['Close'].pct_change().round(4)
df['ma_7'] = df.groupby('ticker')['Close'].transform(lambda x: x.rolling(7).mean()).round(2)
df = df.dropna()

# Load
print("Loading to PostgreSQL...")
engine = create_engine(DB_URL)
df.to_sql('stock_prices_docker', con=engine, if_exists='replace', index=False)
print(f"✅ Loaded {len(df)} rows!")
