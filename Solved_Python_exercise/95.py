'''
Input: 
0001010
0101010

Output:
0101010
'''

t = input()
t2 = input()
string = ''
for i in range(len(t)):
    if t[i] == '1' or t2[i] == '1':
        string+= '1'
    else:
        string +='0'
print(string)