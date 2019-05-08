def select_sort(list):

    while True:

        for i in range(len(list)-1):
            j = i+1
            if list[i] > list[j]:
                list[j],list[i] = list[i],list[j]
            else:
                pass
        
        if list[0] is min(list):
            break
    
    return list


list= [8,9,6,7,5,1,3,4,2]
list = [i for i in range(1000,0,-1)]
print(select_sort(list))