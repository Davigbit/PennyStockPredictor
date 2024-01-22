import requests
import pandas as pd
from key import api_key

symbol = "SPY"
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={api_key}'
r = requests.get(url)
data = r.json().get("Time Series (Daily)", {})

df_SPY = pd.DataFrame([
    {"date": date, "value": float(data[date]["4. close"])}
    for date in data
])

df_SPY['date'] = pd.to_datetime(df_SPY['date'])

df_SPY.to_csv("S&P 500.csv", index=False)