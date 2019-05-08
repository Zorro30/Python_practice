'''
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''

upper =0
lower =0
string = input ("Enter the string combination of letters and numbers:")
strings = ','.join(string)
for i in strings:
    if i.isupper():
        upper +=1
    elif i.islower():
        lower +=1

print (upper,lower)