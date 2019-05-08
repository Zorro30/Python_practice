def print_any(*args):
    arg1= args
    print ('arg1: {!r}'.format(arg1))

def print_two(arg1,arg2):
    print ('arg1: {!r}, arg2: {!r}'.format(arg1,arg2))

def print_one(arg1):
    print ('arg1: {!r}'.format(arg1))


#gau = input('Enter the arguments you want separated by ",":')
#print_any(gau)
print_any(input('Enter your arguments:'))
#print_one("gau")