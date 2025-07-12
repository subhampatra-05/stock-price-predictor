# 📈 Stock Price Predictor (AI/ML Project)

This is a backend-only machine learning project that predicts the next day's stock closing price based on historical stock data. It uses Python, scikit-learn, and yfinance to fetch, train, and predict without any frontend.

## 🔧 Features

- ✅ Predicts next-day closing price for any valid stock ticker (e.g., AAPL, GOOGL)
- ✅ Fetches real-time historical stock data using yfinance
- ✅ Trains a regression model (Random Forest)
- ✅ Supports multiple stocks — each model is saved individually
- ✅ Includes error handling for invalid tickers

## 💻 How to Run This Project

### 1. Set up virtual environment

(in terminal)

python -m venv venv

venv\Scripts\activate   &nbsp;&nbsp;    (# or source venv/bin/activate for Mac/Linux)

### To deactivate venv 

(in terminal)

deactivate
##
### 2. Install dependencies

(in terminal)

pip install -r require.txt
##
### 3. Fetch data 

(in terminal)

python fetch.py
##
### 4. Training model

(in terminal)

python train_model.py
##
### 5. Predict stock price

(in terminal)

python predict.py
##
### Sample output

Enter stock (e.g. AAPL, GOOGL, MSFT): msft 

 Predicting next close price for MSFT
 
Open: 498.47

High: 505.02

Low: 497.79

Close: 503.32

Volume: 16455000

Volume: 16455000

 Predicted next closing price for MSFT: $501.34
