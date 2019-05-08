'''You must ouput the sum of the first N even natural numbers.
For example, if N=4 we get 2, 4, 6, 8 and the sum of these numbers is 20.
'''

n = int(input())
count = 0
i = 1
total = 0
while count < n:
    if i%2 == 0:
        total +=i
        count +=1
    i +=1
print(total)
