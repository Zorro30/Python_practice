"""
The Birds Language have only one rule : after each vowels(a,e,i,o,u,A,E,I,O,U) you should insert letter p and that vowels one more time. For a given String convert it to Birds Language.
Input
alex
Output
apalepex 
"""
sentence = input()
new = ''
for i in sentence:
    if i in ('aAeEIiOoUu'):
        new += i+'p'+i
    else:
        new +=i
print(new)

# list comphrension
for i in input():print(i+'p'+i if i in 'aAeEIiOoUu' else i,end='')