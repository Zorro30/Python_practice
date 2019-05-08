def arm_number(n):
    tot = 0
    for i in str(n):
        tot += int(i)**3
    if tot == n:
        print('Is armstrong')
    else:
        print('Not armstrong')

arm_number(int(input('Enter the number to check if its Armstrong or Not: ')))