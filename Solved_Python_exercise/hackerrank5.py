
def getTotalX(a,b):
    count = 0
    for i in range(max(a),max(b)+1):
        if all(i%ar ==0 for ar in a) and all(br%i ==0 for br in b):
            count+=1
    return(count)

n,m = input().split(' ')
a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))

total = getTotalX(a, b)
print(total)