'''
Converting ascii value into a string of words.
eg:
Input: 72 101 108 108 111 32 87 111 114 108 100
output: Hello World
'''

deck = ''

for i in input("Enter the Ascii value which you wish to convert into a sentence:").split():
    char_code = int(i)
    val = chr(char_code)
    deck += val

print(deck)