'''
Input
5 2
Output
1 2 4 8 16
'''

n, r = [int(i) for i in input().split()]
fin = [1]
prev = 1
for i in range(n-1):
    add = r*prev
    fin.append(add)
    prev = add
print(' '.join(str(s) for s in fin))