'''
Print + in shape of a square, and let the size of square given by the user.
eg:
Input:
> 3
Output:
+++
+++
+++
'''

s = int(input("Enter the size of square you want:"))
for i in range(s):
    print ('+'*s)