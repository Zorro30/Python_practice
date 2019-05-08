"""
You have intercepted an enemy communication signal, but it is encrypted. However, you know that the message was encrypted using the following algorithm:

For every letter in the message M, an integer E representing the distance away from the letter z in the English alphabet is outputted onto a new line. Spaces are given a value of -1.

You must decrypt this communication, or risk losing the war!

Input
5
18
21
14
14
11
Output:
hello
"""

n = int(input())
word = ''
for i in range(n):
    e = int(input())
    if e == -1:
        word += ' '
    else:
        num = 122 - e
        word += chr(num)
print(word)