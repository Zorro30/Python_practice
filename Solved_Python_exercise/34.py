'''
Input: 12234441
Output: 1234
'''

n = input()

a=''

for i in n:
    if i!=a:
        print(end=i)
    a=i
