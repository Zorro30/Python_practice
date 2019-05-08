'''
Finding the greatest common divisor, 
eg :
input:
1000000 5
output: 
5
'''

a, b = [int(i) for i in input().split()]
lis = list()
for i in range(1,a):
    if a%i == 0 and b%i == 0:
        lis.append(i)
print(lis[-1])