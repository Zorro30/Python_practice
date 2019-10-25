def getType(abc):
    # Write your code here

    fin = []
    for i in abc:
        res = list(i for i in i.split(' '))
        if res[0]==res[1]==res[2]:
            fin.append("Equilateral")
        elif res[0]==res[1] and res[2]<res[1]+res[0] or res[1]==res[2]and res[0]<res[1]+res[2] or res[2]==res[0] and res[1]<res[0]+res[2]:
            fin.append("Isosceles")
        else:
            fin.append("None of these")
    print(fin)

getType(
["2 2 1",
"48 16 48",
"48 99 48",
"12 12 12",
"1 1 3"])