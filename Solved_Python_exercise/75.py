'''
input : azxxzyyyddddyzzz
output: azzz
'''
n = input().lower()
for i in n:
    d = 0
    if n.count(i) == 2 or n.count(i) == 4 or n.count(i) == 6: 
        n = n.replace(i,'')
print(n)