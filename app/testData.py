#testData.py
import yfinance as yf

def retrieve_data(stock_symbol):
    # Create a Ticker object
    ticker = yf.Ticker(stock_symbol)

    # Retrieve real-time price data
    real_time_data = ticker.history(period="1d")

    # Retrieve historical price data for a specific date range
    start_date = "2022-01-01"
    end_date = "2022-01-31"
    historical_data = yf.download(stock_symbol, start=start_date, end=end_date)

    # Retrieve balance sheet, income statement, and cash flow data
    balance_sheet = ticker.balance_sheet
    income_statement = ticker.income_stmt  # Updated attribute name
    cash_flow = ticker.cashflow

    # Retrieve hourly price data for a specific date
    hourly_data = ticker.history(period="1d", interval="1h")

    # Print the retrieved data
    print("Real-Time Price Data:")
    print(real_time_data)

    print("\nHistorical Price Data:")
    print(historical_data)

    print("\nBalance Sheet Data:")
    print(balance_sheet)

    print("\nIncome Statement Data:")
    print(income_statement)

    print("\nCash Flow Data:")
    print(cash_flow)

    print("\nHourly Price Data:")
    print(hourly_data)

if __name__ == "__main__":
    stock_symbol = "AAPL"  # Replace with the stock symbol you want to test
    retrieve_data(stock_symbol)
