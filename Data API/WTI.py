import requests
import pandas as pd
from key import api_key

symbol = "WTI"
url = f'https://www.alphavantage.co/query?function={symbol}&interval=daily&apikey={api_key}'
r = requests.get(url)
data = r.json()

df_WTI = pd.DataFrame(data["data"])

df_WTI['date'] = pd.to_datetime(df_WTI['date'])

df_WTI.to_csv("../Data CSV/WTI.csv", index=False)