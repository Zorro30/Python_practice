""" 
You must output the sum digits of the power between two input number.

Example:

Input:
2
7

Output:
11
Input
Line 1: An integer X for the base.
Line 2: An integer Y for the exponent.
Output
A single line containing the sum of all digits from the result of X^Y 
"""


x = int(input())
y = int(input())
total = str(x**y)
count = 0
for i in total:
    count += int(i)
print(count)