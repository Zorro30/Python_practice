""" Given a number N and another number P, find the biggest integer M such that P^M ≤ N

For example, if N is 33, and P is 2, the output will be 5, as 2^5=32 """

n = int(input())
p = int(input())
tot = []
for i in range(n):
    if n>=p**i:
        tot.append(i)
print(tot,tot[-1])
