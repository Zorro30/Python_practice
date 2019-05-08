'''
Input: 
2
3
1 2 3
4 5 6

Output:
1 4
2 5
3 6

transposing them in a traditional way.
'''

l = int(input())
h = int(input())
large_list = list()
for i in range(l):
    small_list = list()
    for j in input().split():
        small_list.append(int(j))
    large_list.append(small_list)

for i in range(h):
    hell = list()
    for j in range(len(large_list)):
        new = large_list[j][i]
        hell.append(new)
    print(' '.join(str(x) for x in hell))