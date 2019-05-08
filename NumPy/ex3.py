# this file contains the mathematical operations with array.

import numpy as np

a = np.array([[1,2],[4,5]])

b = np.array([[10,11],[12,13]])

print('addition is \n{}'.format(a+b))
print('subtraction is \n{}'.format(a-b))
print('divison is \n{}'.format(a/b))
print('multiplication is \n{}'.format(a*b))

print('Dot product is  \n{}'.format(np.dot(a,b,out=None)))