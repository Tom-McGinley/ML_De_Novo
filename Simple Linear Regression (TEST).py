#Linear Regression implementation
import numpy as np

def predict(alpha:float, beta:float, x_i:float):
    return beta*x_i + alpha

def error(alpha:float, beta:float, x_i: float, y_i:float):
    return y_i - predict(alpha, beta, x_i)

def sse(alpha:float, beta:float, x: np.array, y: np.array):
    assert len(x) == len(y)
    sqr_errors = [error(alpha, beta, x_i, y_j)**2 for x_i, y_j in zip(x, y)]
    return sum(sqr_errors)

def least_squares_fit(x: np.array, y: np.array):
    return null

