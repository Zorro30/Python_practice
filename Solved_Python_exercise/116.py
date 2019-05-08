'''
print the digital number of a given particular input.
85 => 8+5 = 13 => 1+3 = 4
add the individual digit until you get a single digit out of it.
eg:
input: 85
output: 4
'''

n = input()
def digital(num):
    tot = 0
    for i in str(num):
        tot += int(i)
    if len(str(tot)) == 1:
        print(tot)
    else:
        digital(tot) 

digital(n)