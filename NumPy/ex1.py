#getting started with Numpy
# This file contains the basic way to create a array, and also the methods to check the size and datatypes of the array.

import numpy as np

a = np.array([[1,2,3],[4,5,6]])
print(a)
print('Shape is {}'.format(a.shape))
print('Data type is {}'.format(a.dtype))
print('Size of the array is {}'.format(a.size))

b = np.ones([2,3])
print(b)

c = np.zeros([2,3])
print(c)

d = np.linspace(1,5,5)
print('Uisng linspace {}'.format(d))

e = np.arange(6,10)
print('Using Range {}'.format(e))

# to reshape the array and change it to one dimensional

print(a.reshape(3,2)) # reshaping
print(a.ravel()) # changing it to one dimensional