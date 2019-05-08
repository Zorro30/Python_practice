'''
eg:
Input:
4
mxxx
xaxx
xxix
xxxn
Output:
main xxxx
'''

n = int(input())
premier,demier= '',''
i ,j = 0, n-1
for i in range(n):
    line = input()
    premier  += line[i]
    i +=1
    demier+=line[j]
    j -=1

print(premier,demier)