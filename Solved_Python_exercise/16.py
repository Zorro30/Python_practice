#Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.

def bin_search (li,element):
    bottom = 0
    top = len(li)-1
    index = -1
    while top >= bottom and index ==-1:
        mid = int(top+bottom/2.0)
        if li[mid] == element:
            index = mid
        elif li[mid] > element:
            top = mid-1
        elif li[mid] < element:
            bottom = mid+1
    return index

li = [2,3,4,5,6,7,8]
print (bin_search(li,5))