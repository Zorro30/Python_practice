'''Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''
Letters =0
digits =0
string = input ("Enter the string combination of letters and numbers:")
strings = ','.join(string)
for i in strings:
    if i.isalpha():
        Letters +=1
    elif i.isnumeric():
        digits +=1

print (Letters,digits)