#chart_functions.py
def moving_average(data, period):
    # Calculate the moving average
    # 'data' is expected to be a list of closing prices
    return [sum(data[i:i+period])/period for i in range(len(data) - period + 1)]

def rsi(data, period):
    # Calculate the Relative Strength Index (RSI)
    gains, losses = [], []
    for i in range(1, len(data)):
        change = data[i] - data[i-1]
        if change > 0:
            gains.append(change)
        else:
            losses.append(abs(change))
    
    average_gain = sum(gains[-period:]) / period
    average_loss = sum(losses[-period:]) / period
    rs = average_gain / average_loss
    return 100 - (100 / (1 + rs))

# ... additional indicator functions ...

def get_available_indicators():
    return ["MA", "RSI", "EMA", "Bollinger Bands"]  # Add more as needed

def fetch_chart_data(ticker, indicators, interval):
    # Fetch historical price data, calculate indicators, and format the data
    # You can use your existing functions and data for this
    chart_data = {
        'labels': ['Label 1', 'Label 2', 'Label 3'],  # Replace with your data labels
        'datasets': [{
            'label': 'Dataset 1',
            'data': [10, 20, 30],  # Replace with your data
            'backgroundColor': 'rgba(255, 99, 132, 0.2)',
            'borderColor': 'rgba(255, 99, 132, 1)',
            'borderWidth': 1
        }]
    }
    return chart_data