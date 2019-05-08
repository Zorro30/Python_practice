'''
eg:
input: 
3
4
5
1
output:
5
4
1
'''

n = int(input())
total =[]
for i in range(n):
    x = int(input())
    total.append(x)
    total.sort(reverse = True)
print(' '.join(str(x) for x in total))