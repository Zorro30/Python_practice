'''
Password checker
1) It must contain more than 3 characters and less than or equal to 20 characters.
2) It must conatin more than or equal to 3 alphabets.
'''

username = input()
count = 0
valid = False
if 3 <= len(username) < 20:
    for i in username:
        if i.isalnum:
            if i.isdigit():
                count+=1
            if len(username) - count >= 3:
                valid = True
            else:
                valid = False
                break
        else:
            valid = False
            break
else:
    valid = False

if valid:
    print('VALID')
else:
    print('INVALID')
