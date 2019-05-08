'''
You must help Gary move X boxes. He can carry one box per N minutes, 
but he only has T hours to do so. You promised to help, but since you're very lazy, 
you will only carry the minimum number of boxes that are required for Gary to finish.
'''

x = int(input())
n = int(input())
t = int(input())

if t == 0:
    print(x)
else:
    if ((x*n)/60) < t:
        print('0')
    else:
        box_moved = t*60//n
        print(int(x-box_moved))