'''John works at a clothing store. He has a large pile of socks that he must pair by color for sale.
Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
For example, there are  socks with colors . There is one pair of color  and one of color .
There are three odd socks left, one of each color. The number of pairs is .

eg
input:
9
10 20 20 10 10 30 50 10 20

output:
3
'''
def sockMerchant( ar):
    val = []
    for i in ar:
        if ar.count(i) in range(1,100,2):
            val.append(i)
    print((len(ar)-len(set(val)))//2)

ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
sockMerchant(ar)