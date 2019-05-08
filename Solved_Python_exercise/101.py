'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up.
eg:
input:
5
-3 -8 -1 -2 -3
output:
-2
'''

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split(' ')))
    max_num = max(arr)
    while max(arr) == max_num:
        arr.remove(max_num)

    print(max(arr))