'''
input = 123
output: True
input = 987
output = false
'''


n = input()
flag_check = False
for i in range(len(n)-1):
    if n[i] <= n[i+1]:
        if n[i] <= n[-1]:
            flag_check = True
    else:
        if n[i] > n[i+1]:
            print('False')
            break
            

if flag_check:
    print('True')
    