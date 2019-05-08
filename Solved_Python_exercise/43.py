'''
Print the sum of digits of a decimal number converted to binary.
Example: 15 in decimal => 1111 in binary, output will be 4.
'''

n = int(input())
print(bin(n).count('1'))