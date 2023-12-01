#populateDB.py
import yfinance as yf
import requests_cache
from models import MarketData
from db import db
from app import app
from pyrate_limiter import Limiter, RequestRate, Duration
from requests_ratelimiter import MemoryQueueBucket
from datetime import datetime, timedelta

# Create a CachedSession with rate limiting to avoid rate limiting from Yahoo
session = requests_cache.CachedSession('yfinance.cache')
session.headers['User-agent'] = 'my-program/1.0'

# Define rate limiting settings (adjust these as needed)
requests_per_second = 2
seconds_between_requests = 5
session.limiter = Limiter(RequestRate(requests_per_second, Duration.SECOND * seconds_between_requests))
session.bucket_class = MemoryQueueBucket

# Create a Ticker object with the custom session
def create_ticker(ticker):
    return yf.Ticker(ticker, session=session)

# Create an application context
with app.app_context():
    # List of tickers to fetch data for
    tickers = ['AAPL', 'GOOGL', 'MSFT', 'TSLA']

    def fetch_and_store_data(ticker):
        try:
            # Create a Ticker object
            market_data = create_ticker(ticker)

            # Fetch 1-hour interval historical market data using the adjusted date range
            historical_data = market_data.history(period="1d", interval="1h", auto_adjust=True)
            
            # Extract options expiration dates (if needed)
            options_data = market_data.options

            # Check if the ticker already exists in the database
            existing_data = MarketData.query.filter_by(ticker=ticker).first()

            if existing_data:
                # Update existing data
                existing_data.historical_data = historical_data.to_json(orient='split')
                existing_data.options_data = options_data
            else:
                # Create new market data entry
                new_data = MarketData(
                    ticker=ticker,
                    historical_data=historical_data.to_json(orient='split'),
                    options_data=options_data
                )
                db.session.add(new_data)

            db.session.commit()

            # Display some sample historical data for analysis
            print(f"Successfully updated market data for {ticker}")
            print(f"Ticker: {ticker}")
            print("Sample Historical Data:")
            print(historical_data.head())  # Print the first few rows of historical data
            print("Options Expiration Dates:")
            print(options_data)
            print("\n")
        except Exception as e:
            print(f"Error populating data for {ticker}: {e}")

    # Iterate through tickers and fetch data
    for ticker in tickers:
        fetch_and_store_data(ticker)

    # Close the database session
    db.session.close()
