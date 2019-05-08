'''
eg: 
There are  hourglasses in , and an hourglass sum is the sum of an hourglass' values. 
Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.
input: 
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

output:
19
========

input: 
0 -4 -6 0 -7 -6
-1 -2 -6 -8 -3 -1
-8 -4 -2 -8 -8 -6
-3 -1 -2 -5 -7 -4
-3 -5 -3 -6 -6 -6
-3 -6 0 -8 -6 -7

output:
-19
'''
import sys
arr = []
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

maxi = -sys.maxsize-1
for p in range(1,5):
    for i in range(1,5):
        temp = arr[p][i]+arr[p-1][i-1]+arr[p-1][i]+arr[p-1][i+1]+arr[p+1][i-1]+arr[p+1][i]+arr[p+1][i+1]
        if temp > maxi:
            maxi = temp
print(maxi)