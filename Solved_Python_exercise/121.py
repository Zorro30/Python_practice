'''
Input:
10
-64
71
-98
-60
-18
41
88
-2
-24
63

Output:
-63
71
-97
-59
-17
41
89
-1
-23
63
'''

m = int(input())
res = []
for i in range(m):
    n = int(input())
    if n >= 0 and n%2==0:
        print(n+1)
    elif n<0 and n%2==0:
        print(n+1)
    elif n<0:
        print(n)
    elif n>0:
        print(n)
