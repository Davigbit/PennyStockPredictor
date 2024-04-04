import requests
import pandas as pd
from key import api_key
import os
from datetime import datetime, timedelta

symbol = "NATURAL_GAS"
url = f'https://www.alphavantage.co/query?function={symbol}&interval=daily&apikey={api_key}'
r = requests.get(url)
data = r.json()

df_NG = pd.DataFrame(data["data"])

df_NG['date'] = pd.to_datetime(df_NG['date'])

df_NG['value'] = pd.to_numeric(df_NG['value'], errors='coerce')

df_NG = df_NG.sort_values(by='date')
yesterday = datetime.now() - timedelta(days=1)
yesterday_str = yesterday.strftime('%Y-%m-%d')
filtered_df = df_NG[df_NG['date'] < yesterday_str]
all_dates = pd.date_range(start=filtered_df['date'].min(), end=yesterday, freq='D')
all_dates_df = pd.DataFrame({'date': all_dates})
merged_df = pd.merge(all_dates_df, df_NG, on='date', how='left')
merged_df['value'] = merged_df['value'].fillna(method='ffill')

script_directory = os.path.dirname(os.path.abspath(__file__))
project_directory = os.path.dirname(script_directory)
output_file = os.path.join(project_directory, "Data CSV", "Natural Gas.csv")
merged_df.to_csv(output_file, index=False)