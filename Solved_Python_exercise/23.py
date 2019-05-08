'''
Input
Line 1 : The number of values N to handle.
N next lines : An integer X on each line.

Output
For each integer X, the number of ones in its binary representation.
'''
counts = {}
n = int(input())
for i in range(n):
    x = int(input())
    binary = str(bin(x))
    val = (binary).count('1')
    counts[x] = val 
print(counts)