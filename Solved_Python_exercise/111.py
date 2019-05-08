'''
input: 
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
output:
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
'''

string, max_width = input(), int(input())
for i in range(0,len(string),max_width):
    print(string[i:max_width+i])