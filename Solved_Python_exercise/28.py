'''
Given a String you must output the average ASCII value of that string. For example :
input: "abc"
output: 104
'''
a =0
n = input()
for i in n:
    a += ord(i)

print (int(a)//len(n))