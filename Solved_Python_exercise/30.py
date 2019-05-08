'''
Goal is to build an interactive interpreter for simple programming language, which uses the following statements:

Statements:
inc - adds 1 to variable
dec - subtracts 1 from variable
print - prints the variable (value) without space
exit - ends the input
double - variable is multiplied by 2
half - variable is divided by 2

The starting value is 0.


eg: 
input:
inc inc dec inc print exit

output:
2

'''
val = 0
for i in input().split():
    if i == 'inc':
        val+=1
    elif i == 'dec':
        val-=1
    elif i == 'print':
        print (val)
    elif i == 'double':
        val*=2
    elif i == 'half':
        val//=2
    elif i == 'exit':
        break
