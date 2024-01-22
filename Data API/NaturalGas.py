import requests
import pandas as pd
from key import api_key

symbol = "NATURAL_GAS"
url = f'https://www.alphavantage.co/query?function={symbol}&interval=daily&apikey={api_key}'
r = requests.get(url)
data = r.json()

df_NG = pd.DataFrame(data["data"])

df_NG['date'] = pd.to_datetime(df_NG['date'])

df_NG.to_csv("Natural Gas.csv", index=False)