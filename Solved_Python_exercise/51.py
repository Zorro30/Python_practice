'''
Input
Line 1: Two integers w and h for the width and height of the grid.
Line 2: Two integers x1 and y1 for point 1.
Line 3: Two integers x2 and y2 for point 2.
Output
The grid as explained in the statement.
Constraints
1 ≤ w ≤ 20
1 ≤ h ≤ 20
Example
Input
7 7
1 2
3 4
Output
.......
.......
.+++...
.+++...
.+++...
.......
.......
'''

w, h= [int(i) for i in input().split()]
a, b = [int(i) for i in input().split()]
c, d = [int(i) for i in input().split()]

for i in [["+" if  a<=x<=c and b<=y<=d else "." for x in range(w)] for y in range(h)]:
    print(''.join(i))





