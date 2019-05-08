import math
index = []

for i in range(1,100000):
    val = input("Enter a value: ")

    if val =='done':
        break
    else:
        x = int(val)
        p = -1*(x*math.log(x))
        index.append(p)
        
print ("The value of index is %s:"%index)