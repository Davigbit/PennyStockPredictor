import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import subprocess

subprocess.run(['python', 'Data.py'])

from Data import df_before_2023 as df

#plt.figure(figsize=(6,4))
#sns.heatmap(df.corr(), cmap='Blues', annot=True, fmt=".2f")

X = df.drop('BTE_change', axis=1)
Y = df['BTE_change'].astype(int)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, shuffle=True, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

random_forest_model = RandomForestClassifier(class_weight='balanced', random_state=42)
random_forest_model.fit(X_train_scaled, Y_train)

Y_pred_rf = random_forest_model.predict(X_test_scaled)
binary_predictions_rf = np.round(Y_pred_rf).astype(int)

accuracy_rf = accuracy_score(Y_test, binary_predictions_rf)
print(f'Accuracy on Validation Set: {accuracy_rf}')
print(classification_report(Y_test, binary_predictions_rf))