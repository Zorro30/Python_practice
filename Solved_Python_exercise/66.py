""" Input
A single binary number T (0b followed by a string of 1's and 0's). The string length is N.
Output
A hexadecimal representation of the binary number (0x followed by a string of chars in 0123456789abcdef) """

num = input()[2:]
print(hex(int(num,2)))

