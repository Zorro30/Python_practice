def minimumSwaps(arr):
    swap = 0
    i = 0 
    while i <len(arr):
        if arr[i] == i+1:
            i+=1
            continue
        arr[arr[i]-1], arr[i] = arr[i], arr[arr[i]-1]
        swap+=1
    return swap

n = int(input())

arr = list(map(int, input().rstrip().split()))

res = minimumSwaps(arr)
print(res)
