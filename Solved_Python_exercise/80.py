'''
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix  is shown below:

1 2 3
4 5 6
9 8 9
The left-to-right diagonal = 1+5+9 =15. The right to left diagonal =9+5+3=17 . Their absolute difference is |15-17|=2 .
'''
def diagonalDifference(arr):
    right = 0
    left = 0
    j = n - 1
    for i in range(n):
        right += arr[i][i]
        left += arr[i][j]
        j -= 1

    final = abs(right-left)
    return final

n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)
print(result)