'''
The first line contains two space-separated integers  and ,
the size of  and the number of left rotations you must perform. 
eg:

input: 
5 4
1 2 3 4 5

output:
5 1 2 3 4
'''
nd = input().split()

n = int(nd[0])

d = int(nd[1])

a = list(map(int, input().rstrip().split()))

val = a[:d]
new = a[d:]    
print(new + val)