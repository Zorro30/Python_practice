""" 
01 Test 1
I am
3
02 Test 2
I like trains
11
03 Test 3
Hello world!
10
04 Test 4
Cod1nGam3
7
05 Test 5
message[0]
7
06 Test 6
01100010
0 
"""

message = input().replace(' ','')
str1 = ''
for i in message:
    if i.isalpha():
        str1 = str1 + i
print(len(str1))