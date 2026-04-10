##to create my own unfunc is basically just creating a function but for arrays.
## use use te np.frompyfunc method to do so

import numpy as np

def add(x, y):
    return x+y

add = np.frompyfunc(add,2,1)


test = (add([1,2,3],[2,3,4]))
print(test)