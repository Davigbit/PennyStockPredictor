from functions import *

df = joblib.load('./pkls/df_before_2024.pkl')

X = df.drop('BTE_change', axis=1).to_numpy().transpose()
X = scale(X)

n, m = X.shape
one_m = 1/m

Y = df['BTE_change'].to_numpy().transpose().reshape(1, m)
Y = np.where(Y == -1, 0, Y)

w = np.zeros((n, 1))
b = 0
J = 0

alpha = 5
alpha_decay_rate = 0.999

w, b, J = optimize(w, b, X, Y, one_m, alpha, alpha_decay_rate, 1000000)
print(J)

joblib.dump(w, './pkls/w.pkl')
joblib.dump(b, './pkls/b.pkl')
