'''

Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

For example, . Our minimum sum is  and our maximum sum is . We would print

16 24
'''

def miniMaxSum(arr):
    maxm = max(arr)
    minm = min(arr)
    maxtotal = 0
    mintotal = 0
    for i in arr:
        if i != maxm:
            maxtotal += i
        if i != minm:
            mintotal += i
    return maxtotal,mintotal

arr = list(map(int, input().rstrip().split()))
# arr = list(map(int,input().split(' ')))
print(miniMaxSum(arr))