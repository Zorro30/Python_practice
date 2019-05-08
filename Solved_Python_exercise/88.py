'''
You have a IP address you have to tell which is the open port.
Since we don't have much time, but we know the addition of the digits and multiplying them with the first digit
will lead us to the open port.

Input:
127.0.0.1
Outpu:
11
'''


ip = input()
total =0
for i in ip:
    if i.isalnum():
        total += int(i)
print(total*int(ip[0]))