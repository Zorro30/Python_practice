'''
input: 
3
1 5 8

output:
1:*
2:
3:
4:
5:*
6:
7:
8:*
9:
'''

n = int(input())
global val
val = ''
for i in input().split(' '):
    val+=i
    
for i in range(1,10):
    if str(i) in val:
        print(str(i)+':*')
    else:
        print(str(i)+':')