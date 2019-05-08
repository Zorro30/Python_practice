'''
Given an array of integers, find the subset of non-adjacent elements with the maximum sum. Calculate the sum of that subset.

For example, given an array arr=[-2,1,3,-4,5] we have the following possible subsets:

Subset      Sum
[-2, 3, 5]   6
[-2, 3]      1
[-2, -4]    -6
[-2, 5]      3
[1, -4]     -3
[1, 5]       6
[3, 5]       8

Our maximum subset sum is 8.

'''

def maxSubsetSum(arr):
    dp = []
    dp.append(arr[0])
    dp.append(max(arr[:2]))
    for a in arr[2:]:
        dp.append(max([ dp[-2]+a, a, dp[-1]]))
    return dp[-1]  

n = int(input())

arr = list(map(int, input().rstrip().split()))

res = maxSubsetSum(arr)
print(res)