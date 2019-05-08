'''
Program must output only the capital letters of the string given as input.

INPUT:
A string S.

OUTPUT:
A string containing S stripped of all characters except capital letters.

Input
.2A1N5Y64! §C*H*zAtrR
Output
ANYCHAR
'''

s = input()
result = ''.join(c for c in s if c.isalpha() and c.isupper())
print (result)