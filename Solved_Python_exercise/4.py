'''
Write a program which accepts a sequence of comma separated 4 digit binary
 numbers as its input and then check whether they are divisible by 5 or not.
  The numbers that are divisible by 5 are to be printed in a comma 
  separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
'''
binary = []
decimal = []
hexadecimal = []
val = input ("Enter 4 digit binary only:").split(',')

for i in val:
    if int(i) % 5==0:
        binary.append(i)
        decimal.append(int(i,2)) #also converting binary to decimal.
        hexadecimal.append(hex(int(i,10)))
print (binary)
print (decimal)
print (hexadecimal)