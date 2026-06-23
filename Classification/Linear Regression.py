#Linear Regression
import numpy as np

X = np.asarray([1,2,3,4]).reshape(-1, 1)
y = np.asarray([40, 50, 55, 70])
print(X)

p = np.linalg.inv(np.asarray(X.T @ X)) @ X.T @ y
print(p)