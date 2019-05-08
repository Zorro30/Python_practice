'''
You can perform the following operations on the string, a:

Capitalize zero or more of a's lowercase letters.
Delete all of the remaining lowercase letters in a.
Given two strings, a and b, determine if it's possible to make a equal to b as described. If so, print YES on a new line. Otherwise, print NO.

For example, given a=AbcDE and b=ABDE, in a we can convert b and delete c to match b. If a=AbcDE and b=AFDE, matching is not possible because letters may only be capitalized or discarded, not changed.

eg:
input:
3
AbCdE
AFE
beFgH
EFG
beFgH
EFH

output:
NO
NO
YES

'''

def abbreviation(a,b):
    num = False
    for i in b:
        if i.lower() in a or i.upper() in a:
            num = True
        else:
            num = False
            return 'NO'
    if num:
        for j in a:
            if j.isupper() and j in b:
                num = True
            elif j.isupper() and j not in b:
                num = False
    if num:            
        return 'YES'            
    else:
        return 'NO'

q = int(input())


for q_itr in range(q):
    a = input()

    b = input()

    result = abbreviation(a, b)
    print(result)