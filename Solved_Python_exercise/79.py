""" 
Find the best investment among the given crypto currencies.
Input
N lines : CryptoName StartValue EndValue
Output
The most profitable CryptoName 

"NONE" if N = 0
Constraints
0 <= N <= 20
Example
Input
2
IOTA 0.4524536149 0.47254123
BTC 6328.29 6428.29
Output
IOTA 
"""

n = int(input())
dict1 = dict()
for i in range(n):
    crypto, sValue, eValue = input().split(' ')
    final = (float(eValue)-float(sValue))/float(sValue)*100
    dict1[crypto] = final
val = max(dict1.items(), key = lambda x:x[1])[0]
print(val)
