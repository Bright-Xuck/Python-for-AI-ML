from numpy import random
import numpy as np

x = random.randint(100)
y = random.rand() * 10

print(x, y)

arr = np.array([1, 2, 3, 4, 5])

random.shuffle(arr)

print(random.permutation(arr))
print(arr)
