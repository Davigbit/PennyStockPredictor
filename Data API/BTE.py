import requests
import pandas as pd
from key import api_key

symbol = "BTE.TO"
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={api_key}'
r = requests.get(url)
data = r.json().get("Time Series (Daily)", {})

df_BTE = pd.DataFrame([
    {"date": date,
    "value": float(data[date]["4. close"]),
    "volume": float(data[date]["5. volume"])}
    for date in data
])

df_BTE['date'] = pd.to_datetime(df_BTE['date'])

df_BTE.to_csv("BTE.csv", index=False)