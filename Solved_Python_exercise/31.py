'''
Your program must switch the case of each character of the given string.

input:
Hello World
output:
hELLO wORLD
'''
val =''
s = input()
for i in s:
    if i.isupper():
        val += i.lower()
    elif i.islower():
        val +=i.upper()
    elif i == ' ':
        val +=' '
    else:
        val +=i
print (val)
