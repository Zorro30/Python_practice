'''
input = ab
output = 195

input = Hello world
output:
500
520
'''

n = input()
total = 0
for i in n:
    if i == ' ':
        print(total)
        total = 0
    else:
        total += ord(i)
    
print(total)

    