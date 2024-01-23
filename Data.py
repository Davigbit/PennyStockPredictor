import os
import pandas as pd

files = ['BTE.csv', 'Interests.csv', 'Natural Gas.csv', 'S&P 500.csv', 'WTI.csv']

dfs = {}

for file in files:
    df_name = f'df_{file.replace(" ", "_").replace(".", "_")}'
    dfs[df_name] = pd.read_csv(os.path.join('./Data CSV/', file), parse_dates=['date'])
    dfs[df_name] = dfs[df_name].sort_values(by='date', ascending=False)
    dfs[df_name] = dfs[df_name][dfs[df_name]['date'] >= '2005-01-04']

for key, df in dfs.items():
    if key != 'df_BTE_csv':
        df['value'] = df['value'].shift(-1)

dfs['df_BTE_csv']['volume'] = dfs['df_BTE_csv']['volume'].shift(-1)

for key, df in dfs.items():
    dfs[key] = df.reset_index(drop=True)

dfs['df_BTE_csv'] = dfs['df_BTE_csv'].rename(columns={'date': 'Date', 'value': 'BTE (CAD)', 'volume': 'BTE Volume'})
dfs['df_Interests_csv'] = dfs['df_Interests_csv'].rename(columns={'value': 'Interest Rate (%)'})
dfs['df_Natural_Gas_csv'] = dfs['df_Natural_Gas_csv'].rename(columns={'value': 'Natural Gas (USD)'})
dfs['df_S&P_500_csv'] = dfs['df_S&P_500_csv'].rename(columns={'value': 'S&P 500 (USD)'})
dfs['df_WTI_csv'] = dfs['df_WTI_csv'].rename(columns={'value': 'WTI (USD)'})

result_df = pd.concat([dfs['df_BTE_csv']['Date'], dfs['df_BTE_csv']['BTE (CAD)'], dfs['df_BTE_csv']['BTE Volume'], 
                       dfs['df_Interests_csv']['Interest Rate (%)'], dfs['df_Natural_Gas_csv']['Natural Gas (USD)'], 
                       dfs['df_S&P_500_csv']['S&P 500 (USD)'], dfs['df_WTI_csv']['WTI (USD)']], axis=1)

result_df = result_df.dropna()

latest_date = result_df['Date'].max()

df_before_2023 = result_df.loc[result_df['Date'] <= '2023-01-01']
df_after_2023 = result_df.loc[result_df['Date'] > '2023-01-01']

df_before_2023.set_index('Date', inplace=True)
df_after_2023.set_index('Date', inplace=True)

print(df_before_2023)