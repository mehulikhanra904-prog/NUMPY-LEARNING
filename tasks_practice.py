import numpy as np

array1= np.array([1,2,3,4,5,6,7,8])
array2= np.array([[5],[6],[7],[8]])
print(array1.shape)
print(array2.shape)
print(array1 * array2)
array = np.array([[1,2,3,4,5]],
                 [[6,7,8,9,10]])
print(np.sum(array))
print(np.mean(array))
print(np.std(array))
print(np.var(array))
print(np.min(array))
print(np.max(array))
print(np.argmin(array))
