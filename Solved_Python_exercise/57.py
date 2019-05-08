""" eg: 
1000
3
-1000 -1 nagative
0 0 null
1 1000 positive
positive """

x = int(input())
n = int(input())
for i in range(n):
    f, t, category = input().split()
    f = int(f)
    t = int(t)
    if x in range(f,t+1):
        print(category)
