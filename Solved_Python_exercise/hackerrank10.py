n = input()
text = ''
for i in n.split(' ')[::-1]:
    text += i[::-1] + ' '
print(text)