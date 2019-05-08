'''
You must output the number in MIDDLE value for each of given lines.
Triplet → Output
1 5 6 → 5
8 4 6 → 6
3 1 3 → 3
2 9 2 → 2
6 6 6 → 6
'''

for i in range(int(input())):
    long = [int(j) for j in input().split()]
    long = sorted(long)
    print(long[1])
    
