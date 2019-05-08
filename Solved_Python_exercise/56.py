'''
Print the number of days present in the given month and year pair.
'''

m = input()
y = int(input())
if m in ('1','3','5','7','8','10','12'):
    print('31')
elif m in ('4','6','9','11'):
    print('30')
elif m == '2' and y%4==0 and y%100 == 0 and y%400 == 0:
    print('29')
elif m == '2' and y%4==0 and y%100!=0:
    print('29')
else:
    print('28')