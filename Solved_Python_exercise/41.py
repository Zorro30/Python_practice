'''
eg:
Input:
2
123006
111222
Output:
true
false
'''

n = int(input())
val = 0
val1= 0
for i in range(n):
    t = input()
    for i in (t[:3]):
        val+=int(i)
    for i in (t[3:]):
        val1+=int(i)
    if val == val1:
        print('true')
    else:
        print('false')