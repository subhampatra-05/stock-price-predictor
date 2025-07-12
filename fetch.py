import yfinance as yf
import pandas as pd
from datetime import datetime

stk = input("Enter stock (e.g. AAPL, GOOGL, MSFT): ").upper()

try:
    end_date = datetime.today().strftime('%Y-%m-%d')
    data = yf.download(stk, start="2018-01-01", end=end_date , auto_adjust=True)

    if data.empty:
        raise ValueError("No data found. Please check the stock name.")
    
    csv_name = f"stocks/{stk}_stock.csv"
    data.to_csv(csv_name)
    print(f" Data for {stk} saved to {csv_name}")
except Exception as e:
    print(f"Error: {e}")
    print("Please enter a valid stock name (e.g. AAPL, GOOGL, MSFT).")