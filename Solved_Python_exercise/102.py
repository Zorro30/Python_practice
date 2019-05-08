'''
to print XOR for two binary numbers.
eg:
input:
001 011
output:
010
'''
n_1, n_2 = input().split()
result = ''
for i in range(len(n_1)):
    if n_1[i] == n_2[i] == '1' or n_1[i] == n_2[i] == '0':
        result += '0'
    elif n_1[i] == '1' or n_2[i] == '0' or n_1[i] == '0' or n_2[i] == '1':
        result +='1'
print(result)