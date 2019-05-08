'''
eg:
input:
3+1+2
output:
1+2+3
'''

n = list(input().split('+'))
string = ''
val = sorted(n,key=int)
for i in val:
    string+=i
print('+'.join(string))