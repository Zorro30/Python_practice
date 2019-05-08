'''
Happy Numbers - A happy number is defined by the following process. Starting with any positive integer, replace the number by the sum of the squares of its digits, and 
repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process 
ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers. Display an example of your output here. Find first 8 happy numbers.
Happy Numbers - A happy number is defined by the following process. Starting with any positive integer, replace the number by the sum of the squares of its digits, and 
repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers, 
while those that do not end in 1 are unhappy numbers. Display an example of your output here. Find first 8 happy numbers.
'''

def happy(n):
    list = []
    while n != 1:
        n = sum(int(i)**2 for i in str(n))
        if n in list:
            return False
        list.append(n)
    return True
 

happy_list=[]

for i in range(1,1000):
    if happy(i):
        happy_list.append(i)
print (happy_list)
