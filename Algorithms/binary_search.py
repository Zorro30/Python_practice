'''
In computer science, binary search, also known as half-interval search, logarithmic search or binary chop is
a search alogrithm that finds the position of a target value within a sorted array. Binary search compares 
the target value to the middle element of the array. If they are not equal, the half in which the target cannot
lie is eleminated and the search continues on the remaining half, again taking the middle element to compare the
target value, and repeating this untill the target value is found.
'''

pos = -1
def search(list,num):
    l = 0
    u = len(list)-1
    while l <= u:
        mid = (u+l)//2
        if list[mid] == num:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < num:
                l = mid+1
            else:
                u = mid-1
    return False

list_num = [2,4,6,7,8,10,678,786,789,1000,3562]
print(list_num)
num = int(input('Enter the number whose position you want to find in the above list: '))

if search(list_num,num):
    print('Found at {}'.format(pos+1))
else:
    print('Not Found')