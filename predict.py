import joblib
import pandas as pd

stk = input("Enter stock (e.g. AAPL, GOOGL, MSFT): ").upper()
model_file = f"models/{stk}_model.pkl"
model = joblib.load(model_file)

print(f" Predicting next close price for {stk}")
open_price = float(input("Open: "))
high_price = float(input("High: "))
low_price = float(input("Low: "))
close_price = float(input("Close: "))
volume = float(input("Volume: "))

features =  pd.DataFrame([[open_price, high_price, low_price, close_price, volume]],columns=['Open', 'High', 'Low', 'Close', 'Volume'])
prediction = model.predict(features)[0]

print(f" Predicted next closing price for {stk}: ${round(prediction, 2)}")