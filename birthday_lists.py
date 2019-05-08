birthdays={'Gau':'Nov 1','Patel':'Nov 2','Rang':'Nov 30'}


while True:
    name=input('Enter a name:(keep blank to quit)')
    if name=='':
        break
    if name in birthdays:
        print(birthdays[name]+ ' is the birthday of '+ name)
    else:
        bday=input('I dont know your birthday can you please tell me it?')
        birthdays[name]=bday
        print('Birthday database updated!')

print(birthdays)
