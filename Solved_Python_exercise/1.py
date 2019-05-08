val = input("Enter the dimension separated by , :").split(',')
rowNum = int(val[0])
colNum = int(val[1])

multilist = [[0 for col in range(colNum)]for row in range(rowNum)]

for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col] = row*col

print (multilist)