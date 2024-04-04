import joblib
import numpy as np
import pandas as pd
from tqdm import tqdm

def scale(X):
    n = X.shape[0]
    return (X - X.mean(axis=1).reshape(n, 1)) / X.std(axis=1).reshape(n, 1)

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def optimize(w, b, X, Y, one_m, alpha, alpha_decay_rate, iterations):
    for trial in tqdm(range(iterations)):

        Z = np.dot(w.T, X) + b
        A = sigmoid(Z)
        dZ = A - Y
        dw = one_m * np.dot(X, dZ.T)
        db = one_m * np.sum(dZ)
        w -= alpha * dw
        b -= alpha * db

        J = -one_m * np.sum(Y * np.log(A) + (1 - Y) * np.log(1 - A))

        if trial % 100 == 0:
            alpha *= alpha_decay_rate
    return w, b, J
