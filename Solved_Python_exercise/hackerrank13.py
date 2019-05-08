'''
Input:
2
ababaa  
aa

Output:
11
3
'''

def stringSim(strin):
    og = strin
    count = 0
    bow = []
    for i in range(len(strin)):
        bow.append(strin[i:])
    for m in bow:
        if m==og:
            count+=int(len(og))
        elif m[0] == og[0]:
            k = 1
            count+=1
            if len(m) == 1:
                break
            else:
                while m[k] == og[k]:
                    count+=1
                    k+=1

    print(count)

n = int(input())
for i in range(n):
    strin = input()
    stringSim(strin)