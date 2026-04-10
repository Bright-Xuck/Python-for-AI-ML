import numpy as np


array = np.array([[1,2,7], [3,4,5]]) ##can also use the ndmin parameter
nonarray = [1,2,3,4,5]

print(type(array))
print(array.dtype)
print(array.ndim, nonarray, array, array[0, 1])

##to interrate throught high dimension arrays wu use the np.nditer instead of using nested for loops
for x in np.nditer(array):
 print(x)

 ##array search np.search
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

