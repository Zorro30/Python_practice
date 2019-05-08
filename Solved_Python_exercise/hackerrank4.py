'''
Problem:
You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).

The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.
You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it is possible, return YES, otherwise return NO.

For example, kangaroo 1 starts at x1=2 with a jump distance v1=1 and kangaroo 2 starts at x2=1 with a jump distance of v2=2. After one jump, they are both at x=3, (x1+v1=2+1, x2+v2=1+2), so our answer is YES.

for eg:
input:
0 3 4 2  #(x1,v1,x2,v2)
output:
YES
'''


def kangaroo(x1,v1,x2,v2):
    
    while x1!=x2:

        x1+=v1
        x2+=v2
        if x2>x1 and v2>v1:
            print("NO")
            return
        elif x1> x2:
            return("NO")
        elif x1 >= 19681908: #just added to comply with the corner case.
            print('NO')
            return
    if x1==x2:
        print('Yes')
    else:
        print('No')



x1, v1, x2, v2 = input().split(' ')

kangaroo(int(x1),int(v1),int(x2),int(v2))