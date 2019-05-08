def insertion_sort(list):

    for i in range(len(list)):
        for m in range(i-0,0,-1):
            if list[m] >list[m-1]:
                break
            else:
                list[m],list[m-1] = list[m-1],list[m]
    return list

list = [9,8,7,6,5]
print(insertion_sort(list))
