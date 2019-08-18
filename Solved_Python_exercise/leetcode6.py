"""
Find 4 weights a,b,c,d which can be used to weigh all weights fro 1Kg, 2Kg to 40Kg
"""

import itertools as it
def solve():
    weights = [x for x in range (1,41)]
    all_seq = [x for x in it.combinations(weights,4) if sum(x) is 40]

    for seq in all_seq:
        measured = set()
        for factor in it.product([1,0,-1], repeat=4):
            curSum = sum([seq[i] * factor[i] for i in range(4)])
            if curSum > 0:
                measured.add(curSum)
            
        if len(measured) is 40:
            print("Winner {}".format(seq))
            break

solve()