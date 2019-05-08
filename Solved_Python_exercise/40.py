'''
Remove the Most significant bit from the number.
eg:
Input:
500
Output:
244

solution: 500 in binary is 111110100, therefore removing the MSB i.e. left most digit it become 11110100 (244).
'''
n = int(input())
for i in range(n):
    num = int(input())
    val = bin(num)[3:]
    print(int(val,2))
