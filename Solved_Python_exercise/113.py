'''
eg:
input: 5 2
output: 2 2 1

eg:
input: 34 7
output: 7 7 7 7 7 6
'''

n, k = [int(i) for i in input().split()]
tot = 0
lis = []
if n % k >=0:
    while tot!=n:
        if n-tot < k:
            k = n-tot
            tot +=k
            lis.append(k)
        else:
            tot+=k
            lis.append(k)
else:
    print(n)

print(' '.join(str(i) for i in lis))