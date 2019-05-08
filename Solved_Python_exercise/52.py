'''
Reverse a string without reversing the words indside
'''

n = input().split(' ')
list1=(n[::-1])
string = ' '.join(map(str,list1))
print(string)