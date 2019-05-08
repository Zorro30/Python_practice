'''
input:
ABCDEF
output:
BADCFE
'''
n = input()
for i in range(0,len(n),2):
    n = list(n)
    temp = n[i+1]
    n[i+1] = n[i]
    n[i] = temp
print(''.join(str(x) for x in n))