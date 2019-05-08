""" Line 1 A string s to get the ASCII values from
Output
Line 1 The Average of all the ASCII values in the given string, rounded to one decimal point
Constraints
1 ≤ length of s ≤ 1000
Example
Input
abc
Output
98.0 
"""

n = input()
total = 0
for i in n:
    total += ord(i)
print(round((total/len(n)),1))