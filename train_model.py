import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib

stk = input("Enter stock (e.g. AAPL, GOOGL, MSFT): ").upper()
csv_file = f"stocks/{stk}_stock.csv"

columns = ['Date', 'Close', 'High', 'Low', 'Open', 'Volume']
#df = pd.read_csv("GOOGL_stock.csv", skiprows=3, names=columns)

df = pd.read_csv(csv_file, skiprows=3, names=columns)
df['Date'] = pd.to_datetime(df['Date'])
df.dropna(inplace=True)
df['Target'] = df['Close'].shift(-1)
df = df[:-1]
features = ['Open', 'High', 'Low', 'Close', 'Volume']
X = df[features]
y = df['Target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(f"MSE: {mean_squared_error(y_test, y_pred):.2f}")
print(f"R2 Score: {r2_score(y_test, y_pred):.2f}")
model_file = f"models/{stk}_model.pkl"
joblib.dump(model, model_file)
print(f" Model saved as {model_file}")