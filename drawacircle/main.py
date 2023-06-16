import numpy as np

arr1 = np.random.randn(8, 3)
print(arr1)

arr2 = np.where(arr1 > 0, 1, -1) # if arr1 > 0, then 1, else -1
print(arr2)

arr3 = arr1 > 0
print(arr3)