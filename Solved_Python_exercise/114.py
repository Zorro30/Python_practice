'''
You must output the largest prime of the given list of numbers.
'''

n = int(input())
lis = []
final = []
for i in range(n):
    m = int(input())
    lis.append(m)
    
def prime(num):

    if n >1:
        for i in range(2,num):
            if num%i == 0:
                return False
        else:
            return True

for i in lis:
    if prime(i):
        final.append(i)

print(max(final))