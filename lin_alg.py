# Implementation of basic linear algebra objects and their operations with no external libraries beyond the Python Standard Library
# By: Tom McGinley
# Reference: https://web.stanford.edu/~boyd/vmls/vmls.pdf

from typing import List
from typing import Iterable
import math

class Vector:
    def __init__(self, arr: List):
        self.arr = arr
        self.size = len(arr)

    #Enables iterative behaviour for class
    def __iter__(self):
        for item in self.arr:
            yield item
    
    #Overload operators to do element-wise operations symbolically
    def __add__(self, other):
        if isinstance(other, Vector):
            return [i + j for (i, j) in zip(self.arr, other.arr)]
        elif isinstance(other, (int, float)):
            return [i + other for i in self.arr]
    
    __radd__ = __add__
    
    def __sub__(self, other):
        if isinstance(other, Vector):
            return [i - j for i, j in zip(self.arr, other.arr)]
        elif isinstance(other, (float, int)):
            return [i - other for i in self.arr]
    
    __rsub__ = __sub__
    
    def __mul__(self, other):
        if isinstance(other, (float, int)):
            return [i * other for i in self.arr]
    
    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, (float, int)):
            return [i / other for i in self.arr]
        
    __rtruediv__ = __truediv__

    def __pow__(self, other):
        if isinstance(other, (float, int)):
            return [i ** other for i in self.arr]
    
    __rpow__ = __pow__

#Vector functions
def zero_vec(size: int) -> Vector:
    "Create a zero-valued vector of length size."
    assert size > 0, "Size must be greater than zero."
    return Vector([0 for i in range(size)])

def dot(x: Vector, y: Vector) -> float | int:
    """Calculate the dot-product of two vectors."""
    assert x.size == y.size, "Size of vectors must be identical."
    result = 0
    for i, j in zip(x, y):
        result += i * j
    return result

### Testing ###
x = Vector([1,2,3,4,5])
y = Vector([2,4,6,8,10])

print(x.size)
print(y.size)
print(type(dot(x, y)))
print(sum(x))
#vec_mul = multiply(x,y)
#zero = zero_vec(5)

#print(f"Zero vector: {zero}")
#print(f"Adding two vectors: {vec_add}")
#print(f"Multiplying two vectors: {vec_mul}")
    