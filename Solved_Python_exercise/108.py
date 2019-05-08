'''
eg 1:
input:
8372?9514
output:
6
eg 2:
input:
981453?67
output:
2
'''

n = input()
tot = 0
for i in n:
    if i.isalnum():
        tot += int(i)
print(45-tot)