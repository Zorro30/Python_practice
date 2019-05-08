'''
You receive 4 integers. 
a is the starting number.
b is the increment in between numbers.
c is the number of numbers per line.
d is the number of lines

eg:
input: 
15
2
5
3

output:
15 17 19 21 23
27 29 31 33 35
39 41 43 45 47
'''

a = int(input())
b = int(input())
c = int(input())
d = int(input())

lis = []
count = 0
for i in range(a,10000,b):
    if len(lis) < c: 
        lis.append(i)
        if len(lis) == 5:
            print(' '.join(str(a) for a in lis))
            lis = []
            count += 1
            if count == d:
                break