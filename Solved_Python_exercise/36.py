'''
Given an integer n, find the next integer m with the same number of 1s in its binary expansion as n's. 

For example, for n = 3 (dec) = 11 (bin), the next integer m with two 1s in its binary expansion is 101 (bin) = 5 (dec)

Input
3
Output
5
'''

n = int(input())
val = (bin(n)[2:]).count('1')
n +=1
while bin(n)[2:].count('1')!=val:
    n +=1

print(n)