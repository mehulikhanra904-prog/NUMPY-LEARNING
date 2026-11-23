import os
import sys
import importlib

# This script is named numpy.py, so exclude its directory while importing NumPy.
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path = [path for path in sys.path if os.path.abspath(path or os.curdir) != script_dir]
np = importlib.import_module("numpy")

a = np.array([2,4,5,6,8])
print(a)
print(np.exp(a))
print(np.log(a))
print(np.sin(a))

a = np.ones((2,3))
print(a)
print(np.exp(a))

b = np.array([[1,2,3],[4,5,6]])
print(b)
b = np.full((4,2),8)
print(b)
a = np.ones((2,3))
b = np.full((3,2),8)

print(np.matmul(a,b))
array =np.array([[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12],
                 [13,14,15,16]])
print(array[1:3,1:3])
print(array[1:3,1:3].sum())
print(array[:,0:3])

#scalar arithmetic 
c = np.array([1, 2, 3, 4])
print(c + 2)
print(c - 2)
print(c * 2)
print(c / 2)
#vectorized math functions 
array = np.array([1,0.7,3.8,4.89])
print(np.sqrt(array))
print(np.round(array))
print(np.floor(array))
print(np.ceil(array))
print(np.exp(array))
print(np.log(array))
print(np.sin(array))
print(np.cos(array))
print(np.tan(array))
print(np.arcsin(array))
print(np.arccos(array))
print(np.arctan(array))
print(np.sinh(array))
print(np.cosh(array))
print(np.tanh(array))
print(np.arcsinh(array))
print(np.arccosh(array))
print(np.arctanh(array))
print(np.degrees(array))
print(np.radians(array))
print(np.isfinite(array))
print(np.isinf(array))

#Exercise 
radii = np.array([1, 2, 3, 4, 5])
# Calculate the area of circles with the given radii
print("Area of circles :",np.pi*radii**2)
