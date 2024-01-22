import requests
import pandas as pd
from key import api_key

symbol = "FEDERAL_FUNDS_RATE"
url = f'https://www.alphavantage.co/query?function={symbol}&interval=daily&apikey={api_key}'
r = requests.get(url)
data = r.json()

df_IN = pd.DataFrame(data["data"])

df_IN['date'] = pd.to_datetime(df_IN['date'])

df_IN.to_csv("Interests.csv", index=False)