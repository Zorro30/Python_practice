""" To convert text into 1337 speak, one must replace (whether upper or lower case):
'O' with '0'.
'L' with '1'.
'Z' with '2'.
'E' with '3'.
'A' with '4'.
'S' with '5'.
'G' with '6'.
'T' with '7'.
'B' with '8'.
'Q' with '9'. 

Input
Hello World
Output
H3110 W0r1d
"""
n = input()
for char in['O','L','Z','E','A','S','G','T','B','Q']:
    if char == 'O' and char in n:
        n = n.replace('O','0')
    if char == 'L' and char in n:
        n = n.replace('L','1')
    if char == 'Z' and char in n:
        n = n.replace('Z','2')
    if char == 'E' and char in n:
        n = n.replace('E','3')
    if char == 'A' and char in n:
        n = n.replace('A','4')
    if char == 'S' and char in n:
        n = n.replace('S','5')
    if char == 'G' and char in n:
        n = n.replace('G','6')
    if char == 'T' and char in n:
        n = n.replace('T','7')
    if char == 'B' and char in n:
        n = n.replace('B','8')
    if char == 'Q' and char in n:
        n = n.replace('Q','9')

# n.replace{'O':'0','L':'1','Z':'2','E':'3','A':'4','S':'5','G':'6','T':'7','B':'8','Q':'9'}
print(n)