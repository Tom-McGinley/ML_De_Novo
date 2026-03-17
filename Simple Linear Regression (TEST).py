#Linear Regression implementation
import numpy as np
import numpy.typing as npt
import math

def predict(alpha:float, beta:float, x_i:float):
    return beta*x_i + alpha

def error(alpha:float, beta:float, x_i: float, y_i:float):
    return y_i - predict(alpha, beta, x_i)

def sse(alpha:float, beta:float, x:npt.ArrayLike, y:npt.ArrayLike):
    assert len(x) == len(y)
    sqr_errors = [error(alpha, beta, x_i, y_j)**2 for x_i, y_j in zip(x, y)]
    return sum(sqr_errors)

def least_squares_fit(x:npt.ArrayLike, y:npt.ArrayLike):
    return null

#Loss functions measuring distance
def l1_loss(y:npt.ArrayLike, y_pred:npt.ArrayLike) -> float:
    """Sum of abs values of diff between predicted values and actual values."""
    return sum([abs(y_i - y_pred_i)] for y_i, y_pred_i in zip(y,y_pred))

def mae_loss(y:npt.ArrayLike, y_pred:npt.ArrayLike):
    """Mean absolute error (MAE), average of l1 losses across n observations"""
    assert len(y) == len(y_pred)
    assert len(y) > 0
    return 1/len(y) * l1_loss(y, y_pred)

def l2_loss(y:npt.ArrayLike, y_pred:npt.ArrayLike) -> float:
    """L2 loss, sum of squared difference between actual and predicted values"""
    return sum([(y_i - y_pred_i)**2 for y_i, y_pred_i in zip(y, y_pred)])

def mse_loss(y:npt.ArrayLike, y_pred:npt.ArrayLike) -> float:
    """Mean Squared Error (MSE)"""
    return 1/len(y) * l2_loss(y, y_pred)

def rmse_loss(y:npt.ArrayLike, y_pred:npt.ArrayLike) -> float:
    """Root mean squared error loss function"""
    return math.sqrt(mse_loss(y, y_pred))

#Matrix implementation of linear regression 9multivariate with multiple weights)
def solve_normal(X:np.matrix, y:npt.ArrayLike) -> npt.ArrayLike:
    return np.matrix.inverse((X @ X.T)) @ X.T @ y

X = np.matrix([[0.496714, -0.138264],[0.647689, 1.523030]])
y = np.array([4.200494, 1.205865])

dia = X.T @ X
dia2 = X.T @ y

print(dia)

print(dia2)

print(solve_normal(X,y))