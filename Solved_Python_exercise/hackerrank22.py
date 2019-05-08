import math
def findParkingPrice(entryTime, leavingTime):
    entryhour = int(entryTime.split(':')[0])
    entrymin = int(entryTime.split(':')[1])
    leavinghour = int(leavingTime.split(':')[0])
    leavingmin = int(leavingTime.split(':')[1])

    # timetaken = ((leavinghour*60)+leavingmin) - ((entryhour*60)+entrymin)
    # print(timetaken)
    # print(math.ceil((timetaken-60)/60))
    if timetaken < 1:
        print(2+3)
    else:
        mul = int(math.ceil((timetaken-60)/60))
        print(2+3+4*mul)


entryTime = input()

leavingTime = input()
res = findParkingPrice(entryTime, leavingTime)
