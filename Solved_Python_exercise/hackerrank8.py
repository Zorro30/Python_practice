'''
You are given an array of n integers,ar = [ar[0],ar[1],......,ar[n-1]], and a positive integer, k. Find and print the number of (i,j) pairs where i<j and ar[i] + ar[j] is divisible by k.

For example, ar=[1,2,3,4,5,6] and k = 5. Our three pairs meeting the criteria are [1,4],[2,3] and [4,6].

eg:
input:
6 3
1 3 2 6 1 2
output:
5
'''


def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(len(ar)):
        for j in range(1,len(ar)):
            if (i<j) and (ar[i]+ar[j])%k==0:
                count +=1
    print(count)


n,k = map(int,input().split())
ar = list(map(int, input().rstrip().split()))
result = divisibleSumPairs(n, k, ar)