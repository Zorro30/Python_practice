'''
Your program must insert the given operator (+, -, / or *) at index X of an integer number and output the result of the operation.

The operation is always valid and the result is always an integer. Plus "+" and minus "-" are the only operators that can be inserted at index 0.

INPUT:
A character O, an integer X and an integer N, separated by spaces. O is a mathematical operator from +, -, / and *.

OUTPUT:
The result of the operation obtained by inserting O in N at index X.
'''

o, x, n = input().split()
x = int(x)
n1 = int(n[:x])
n2 = int(n[x:])
if o == '+':
    print(n1+n2)
elif o == '-':
    print (n1-n2)
elif o == '/':
    print(n1/n2)
elif o == '*':
    print(n1*n2)