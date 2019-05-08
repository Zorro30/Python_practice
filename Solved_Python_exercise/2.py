'''items = input("Enter the words separated by , :").split(',')
items.sort()
print (items)
'''

#---------------------------------------------------------
lines = []
while True:
    s = input ("Enter the string OR press 'Enter' to break:")
    if s:
        lines.append(s.upper())
    else:
        break
print (lines)
# for sentence in lines:
#     print(sentence)
    