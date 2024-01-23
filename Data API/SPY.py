import requests
import pandas as pd
from key import api_key
import os
from datetime import datetime, timedelta

symbol = "SPY"
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={api_key}'
r = requests.get(url)
data = r.json().get("Time Series (Daily)", {})

df_SPY = pd.DataFrame([
    {"date": date, "value": float(data[date]["4. close"])}
    for date in data
])

df_SPY['date'] = pd.to_datetime(df_SPY['date'])

df_SPY = df_SPY.sort_values(by='date')
yesterday = datetime.now() - timedelta(days=1)
yesterday_str = yesterday.strftime('%Y-%m-%d')
filtered_df = df_SPY[df_SPY['date'] < yesterday_str]
all_dates = pd.date_range(start=filtered_df['date'].min(), end=yesterday, freq='D')
all_dates_df = pd.DataFrame({'date': all_dates})
merged_df = pd.merge(all_dates_df, df_SPY, on='date', how='left')
merged_df['value'] = merged_df['value'].fillna(method='ffill')

script_directory = os.path.dirname(os.path.abspath(__file__))
project_directory = os.path.dirname(script_directory)
output_file = os.path.join(project_directory, "Data CSV", "S&P 500.csv")
merged_df.to_csv(output_file, index=False)