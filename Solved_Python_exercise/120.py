'''
3
HELLO WORLD

HEL
ELL
LLO
LO 
O W
 WO
WOR
ORL
RLD

'''

n = int(input())
text = input()

if n%2 ==0:
    print(text)
else:
    for i in range(len(text)-n+1):
        print(text[i:i+n])