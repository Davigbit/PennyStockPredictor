import pandas as pd
from Data import df_after_2023 as df
from model import random_forest_model, scaler
from sklearn.metrics import accuracy_score, classification_report
import numpy as np

df_test = df
df_test = df_test.loc[:, df_test.columns != 'BTE_change']
df_test_scaled = scaler.transform(df_test)
Y_pred = random_forest_model.predict(df_test_scaled)
Y_pred = pd.DataFrame(Y_pred)
Y_pred = Y_pred.rename(columns={0: 'Predicted BTE Change'})

Comp = pd.DataFrame()
Sample = pd.DataFrame()

Comp['Predicted BTE Change'] = Y_pred['Predicted BTE Change']
Comp['BTE_change'] = df['BTE_change'].reset_index(drop=True)
Comp.index = df.index

binary_predictions = np.round(Y_pred).astype(int)
accuracy = accuracy_score(df['BTE_change'], binary_predictions)
print(f'Accuracy on Test Set: {accuracy}')
print(classification_report(df['BTE_change'], binary_predictions))


var = 0
for i in range(len(Comp)):
    if Comp.loc[Comp.index[i], 'Predicted BTE Change'] == Comp.loc[Comp.index[i], 'BTE_change']:
        var += 1
    else:
        var -= 1

print(var)