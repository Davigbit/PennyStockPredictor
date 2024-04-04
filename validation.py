from functions import *

df = joblib.load('./pkls/df_after_2024.pkl')

w = joblib.load('./pkls/w.pkl')
b = joblib.load('./pkls/b.pkl')

X = df.drop('BTE_change', axis=1).to_numpy().transpose()
X = scale(X)
m = X.shape[1]

Y = df['BTE_change'].to_numpy().transpose().reshape(1, m)
Y = np.where(Y == -1, 0, Y)

Z = np.dot(w.T, X) + b
A = sigmoid(Z)

predictions = np.where(A > 0.5, 1, 0)
accuracy = np.mean(predictions == Y)

print(f'Accuracy: {accuracy*100:.2f}%')
result = pd.DataFrame({'Prediction': predictions[0], 'Actual': Y[0]})
print(result)
