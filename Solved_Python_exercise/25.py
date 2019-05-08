'''
You are given a single string. You need to convert each character into it's ASCII value and add the odd numbers together.

Example
Input: ABC
A,B,C → 65,66,67
Take odd numbers
65+67=132
'''
add = 0
word  = input()
for i in word:
    a = ord(i)
    if a%2==1: add += a
print (add)


#Optimized Code:
word  = input()
print(sum(ord(i) for i in word if ord(i)%2==1))