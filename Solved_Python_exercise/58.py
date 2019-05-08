n = int(input())

if  n == 1:
    print('1')
else:    
    count = 0
    for i in range(n):
        if i % 2 != 0:
            print(i, end=' ')
            count+=i

    print(count)