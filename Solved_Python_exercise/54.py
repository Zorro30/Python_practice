'''
Input: An integer N
Output: Integer N concatenated with one of [th, st, nd, rd]
Example

Input: 1
Output: 1st
'''

n = int(input())
if  n%10 == 1:
    print('{}st'.format(n))
elif n%10 == 2:
    print('{}nd'.format(n))
elif n%10 == 3:
    print('{}rd'.format(n))
else:
    print('{}th'.format(n))