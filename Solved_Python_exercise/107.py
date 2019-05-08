""" Write a program that prints the sum of all the positive multiples of 3 or 5 or 7 below N.
For example, if N=15 we get 3, 5, 6, 7, 9, 10, 12, 14 and the sum of these multiples is 66.

eg:
Input: 89
Output : 2076
"""

n = int(input())
print(sum([i for i in range(n) if i%3 == 0 or i%5 ==0 or i%7 == 0]))