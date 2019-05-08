""" The program:
Your program must output whether or not the word given contains the same letter. Lowercase and uppercase versions of the same letter should be considered equal.

INPUT:
W a word.

OUTPUT:
true or false

EXAMPLE:
Input
GrEeN
Output
true
"""

n = input().lower()
double_flag = False
for i in n:
    if n.count(i) >= 2: 
        double_flag = True
    else:
        pass
if double_flag:
    print('true')
else:
    print('false')
