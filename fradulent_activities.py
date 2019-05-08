nd = input().split()
n = int(nd[0])
d = int(nd[1])

expenditure = list(map(int, input().rstrip().split()))


def activityNotifications(expenditure,d):
    count = 0
    for i in range(len(expenditure)):
        ram = list(expenditure[i:i+d])
        ram.sort()
        if i+d >= len(expenditure):
            break
        if d%2 == 1:
            # print(expenditure[i+d], ram[d//2])
            if expenditure[i+d] >= ram[d//2] * 2:
                count+=1
        else:
            if expenditure[i+d] >= (ram[int(d/2)] + ram[int(d/2+1)] / 2):
                count+=1
    print(count)

result = activityNotifications(expenditure,d)
