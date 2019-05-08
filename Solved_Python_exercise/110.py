'''
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
eg:
input:
ABCDCDC
CDC
output:
2
'''

n = input()
s = input()

temp = ''
count = 0
for i in range(len(n)):
    temp += n[i]
    if len(temp) == len(s):
        if temp == s:
            count +=1
        temp = temp[1:]
print(count)