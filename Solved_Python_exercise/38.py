'''
Given a digit N, you must print a reverse pyramid with the base containing N times that digit. Each consecutive row containing 1 digit less. 
The result should contain no spaces.
Input:
2
Output:
22
2
'''
n = int(input())
for i in range (n+1):
    print((n-i)*str(n))
# for i in range(n+1):
#     print((i)*str(n))
    