'''
Convert hexadecimal values to text in Python.
eg
Input: 48 65 6C 6C 6F 20 77 6F 72 6C 64 21
Output: Hello world!
'''
n = input()
value = input()
print(bytes.fromhex(value).decode('utf-8'))