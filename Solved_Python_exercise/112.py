'''
eg:
input: codingame
output: cpflrlgtm
'''

l = input()
char = ''
for i in range(len(l)):
    if i == 0:
        char+=l[i]
    else:
        char+=chr(ord(l[i])+i)
print(char)