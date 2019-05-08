s = input()
count_a,count_c,count_t,count_g = 0,0,0,0
for i in s:
    if i == 'A':
        count_a+=1
    elif i == 'C':
        count_c+=1
    elif i =='G':
        count_g+=1
    elif i =='T':
        count_t+=1

print(count_a,count_c,count_g,count_t)
