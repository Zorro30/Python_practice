'''
import numpy

array_1 = numpy.array([[1,2,3],[0,0,0]])
array_2 = numpy.array([[0,0,0],[7,8,9]])

print numpy.concatenate((array_1, array_2), axis = 1)   

#Output
[[1 2 3 0 0 0]
 [0 0 0 7 8 9]]  

Q: You are given two integer arrays of size X and X ( &  are rows, and  is the column). Your task is to concatenate the arrays along axis .
  
 '''


import numpy
m,n,p = input().split(' ')
M = numpy.array([input().split(' ') for i in range(int(m))], int)
N = numpy.array([input().split(' ') for i in range(int(n))], int)
print(numpy.concatenate((M, N), axis =0))