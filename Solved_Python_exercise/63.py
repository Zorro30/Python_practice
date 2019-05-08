'''
You are a gaming character, and you have a lot of money! But you have also too much bronze coins: they take too much space in your pocket.
The solution ? Convert your bronze coins into gold and silver coins in a shop.

G = Gold
S = Silver
B = Bronze
1 G = 100 S
1 S = 100 B.

Example:
You give 204 B to a shop keeper.
He returns you 2 S and 4 B.
'''

g = int(input())
s = int(input())
b = int(input())
g1 = s//100+g
s1 = b//100+s
b1 = b%100
g1=s1//100
s1%=100
g1+=g
print("{}G, {}S, {}B".format(g1,s1,b1))

    