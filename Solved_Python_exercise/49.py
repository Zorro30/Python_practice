'''
Write a program that prints the numbers from 1 to N except for multiples of 5 where
you have to print "Foo" and for the multiples of 7 where you have to print "Bar". 
For numbers which are multiples of both 5 and 7 print "FooBar".
'''

for i in range(1, int(input())+1):
    # print (i)
    if i%5 == 0 and i%7 != 0:
        print('Foo') 
    elif i%7 == 0 and i%5 != 0:
        print('Bar')
    elif i%5 == 0 and i%7 == 0:
        print('FooBar')
    else:
        print(i)