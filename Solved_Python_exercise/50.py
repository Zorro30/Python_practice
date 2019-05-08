'''
Count all the numbers equal to their line number.
The first line number is 0.

Example 1 : 
If input is
1
0 1 2 3 4

Output is 1 because only one 0 is on line 0

Example 2 : 
If input is
2
0 1 2 3 4
1 1 2 3 4

Output is 3 because only one 0 is on line 0 and there are two 1s in line 1 so 1 + 2 = 3
'''

n = int(input())
for i in range(n):
    row = input()
    print(row.count('{}'.format(i)))
    
