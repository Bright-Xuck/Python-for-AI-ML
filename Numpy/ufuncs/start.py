###ufuncs stand for universal functions that have built in functions for the np object
##They are used to perfomr vectorization

import numpy as np

x = np.array([1,2,3,4])
y = np.array([5,6,7,8])
z= np.array([])

z= np.add(x,y)

print(z)