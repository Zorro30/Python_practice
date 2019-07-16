'''
The first line contains two space-separated integers, m and n, the numbers of words in the magazine and the note.
The second line contains m space-separated strings, each magazine[i]. 
The third line contains n space-separated strings, each note[i].

eg: 
input:
6 4
give me one grand today night
give one grand today

output:
Yes
'''
from collections import Counter

def checkMagazine(magazine,note):
    return (Counter(note) - Counter(magazine)) == {}

mn = input().split()

m = int(mn[0])

n = int(mn[1])

magazine = input().rstrip().split()

note = input().rstrip().split()

if checkMagazine(magazine, note):
    print('Yes')
else:
    print('No')