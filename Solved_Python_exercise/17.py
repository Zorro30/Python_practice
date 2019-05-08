decoded_message = ''
val =''
final_message = ''

message = input('Enter the ascii values you want to decode inversely:') #eg: 111 108 108 101 72 32 101 114 101 104 116 32 41 58
for i in message.split(' '):
    message = chr(int(i))
    decoded_message += message

for i in decoded_message.split(' '):
    val = i[::-1]
    space = ' '
    final_message = final_message + val + space

print(final_message)