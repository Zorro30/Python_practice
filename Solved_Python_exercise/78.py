""" The program:
Your program must reverse all the letters of the words in a given sentence.

INPUT:
Line 1: A string S.

OUTPUT:
A string with the characters of each space-seperated word reversed.

CONSTRAINTS:
S contains at least 1 character.
S contains only alphanumeric characters and spaces.
S contains no two words seperated by more than one space, nor does it contain any other whitespace character.

EXAMPLE:
Input
Hello World
Output
olleH dlroW 
"""
n = input().split(' ')
final = ''
for i in n:
    if final == '':
        final += (i[::-1])
    else:
        final += ' ' + (i[::-1])
print(final)
