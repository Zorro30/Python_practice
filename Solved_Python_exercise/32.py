'''
You must output the minimum number of bits required to code given numbers.
Input
2
1
6
Output
1
3
'''

n = int(input())
for i in range(n):
    x = int(input())
    print (len(bin(x)[2:]))
    