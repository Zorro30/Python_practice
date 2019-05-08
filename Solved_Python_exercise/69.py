""" 
Line 1: Two space-separated integers: The starting number a, and n the number of bits to toggle.
Next n lines:One integer x, the index of the bit to toggle. x = 0 indicates the least significant bit.
Output
'a' with all the indicated bits flipped
Constraints
0 ≤ a < 32767
0 ≤ n < 16
0 ≤ x < 16
Example
Input
5 1
2
Output
1 
"""

a, n = (input().split(' '))
for i in range(int(n)):
    try:
        x = int(input())
        temp = list(bin(int(a))[2:])
        if temp[x] == '0':
            temp[x] = 1
        else:
            temp[x] = 0
    except IndexError:
        print('Please input something in range.')
        break
    fin_temp = ''.join(str(x) for x in temp[::-1])        
    print(int(fin_temp,2))