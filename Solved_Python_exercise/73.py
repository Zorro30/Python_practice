"""
The program:
Your program must output a hollow square composed of the # symbol with sides of length N.

INPUT:
N, an integer.

OUTPUT:
A NxNsquare over N lines made of # symbols.

CONSTRAINTS:
0 < N < 100

EXAMPLE:
Input
5
Output
#####
#   #
#   #
#   #
##### 
"""

val = int(input())
if val == 1:
    print('#'*val)
else:    
    print('#'*val)
    for i in range(val-2):
        print('#'+ ' '*(val-2)+'#')
    print('#'*val)