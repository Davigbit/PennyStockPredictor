import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_absolute_percentage_error
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
import subprocess

subprocess.run(['python', 'Data.py'])

from Data import df_before_2023 as df

plt.figure(figsize=(6,4))
sns.heatmap(df.corr(), cmap='Blues', annot=True, fmt=".2f")

train, test = train_test_split(df, test_size=0.4, shuffle=True)

X_train = train.loc[:, train.columns != 'BTE (CAD)']
Y_train = train.loc[:, ['BTE (CAD)']]

X_test = test.loc[:, test.columns != 'BTE (CAD)']
Y_test = test.loc[:, ['BTE (CAD)']]

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

alphas = np.logspace(-1, 1, 500)
param_grid = {'alpha': alphas}

grid_search = GridSearchCV(Ridge(), param_grid, cv=5)
grid_search.fit(X_train_scaled, Y_train)

best_alpha = grid_search.best_params_['alpha']
print(f'Best Alpha: {best_alpha}')

ridge_model = Ridge(alpha=best_alpha)
ridge_model.fit(X_train_scaled, Y_train)

Y_pred = ridge_model.predict(X_test_scaled)

print(f'Mean Absolute Percentage Error: {mean_absolute_percentage_error(Y_test, Y_pred):.3f}%')
print(f'Mean Absolute Error: {mean_absolute_error(Y_test, Y_pred):.3f}')
print(f'R2 Score: {r2_score(Y_test, Y_pred):.3f}')
