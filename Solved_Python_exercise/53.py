n = input()
num = int(input())
half = num//2
list1 =[]
if num <= 2:
    print("CAN'T")

for i in [n if  half==x else "*" for x in range(num)]:
    list1.append(i)
string = ''.join(map(str,list1))
print(string)