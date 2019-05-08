
#simple linked_list
#just to show the task we can perform on a linkedlist.
#I will code a actual linked list in coming time.
series = list()

def insert(n):  #randomly inserts value in list.
    series.append(n)

def delete(index): #delete the value at a particular index.
    del series[index]

def insert_at(index,val): # insert a value at a particular index.
    series.insert(index,val)

insert(102)
insert(20)
insert(30)
insert(40)
insert(50)
insert(60)
delete(3)
insert_at(5,100)
series.sort()
print(series)

