import numpy as np

a = np.array([[1,2,3],[4,5,69]])

print(a.max())
print(a.min())
print(a.sum())

# square root of the array.
print(np.sqrt(a))

# standard deviation.
print(np.std(a))


# axis 0 and axis 1
# axis 0 gives the addition of columns
# axis 1 gives the addition of rows
print(a.sum(axis=0))
print(a.sum(axis=1))