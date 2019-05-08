'''
convert Normal time to Military time.
eg
Input: 7:45:54PM
Output: 19:45:54

Also take care of 12 AM at the midnight, it is represented as 00:00:00.

'''

def timeConversion(s):
    time = (s[-1:-3:-1])[::-1]
    data = int(s[:2])
    if time == 'PM' and data <= 11:
        data +=12
        return str(data)+':'+str(s[-3:2:-1])[::-1]
    elif time == 'PM' and data == 12:
        return '12' + ':' + str(s[-3:2:-1])[::-1]
    if time == 'AM' and data == 12:
        return '00'+':'+str(s[-3:2:-1])[::-1]
    else:
        return str(s[-3::-1])[::-1]

s = input()

result = timeConversion(s)
print(result)