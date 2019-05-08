# You are given two words. Find the first matching character between the two words in respect to the first word, and then output the one with the largest length of the two horizontally and the smallest length vertically (if both words are of the same length then the second word given should be placed horizontally). 

# Both outputs have to separate each character with a space and be all uppercase, all while making a crossword from the two words.

# If the two words given do not having a matching character, then output:
# NO COMMON CHARACTER

# #cinnamon apple  O/P: C I N N A M O N
#                               P
#                               P
#                               L
#                               E

from collections import Counter
words = input()
lists = []
for i in words.split(' '):
    lists.append(i) 

value1 = Counter(lists[0])
value2 = Counter(lists[1][0:1])

common  = value1 & value2
final = list(common.elements())
print (final)
if len(final) == 0:
    print ("Please enter some other strings")
else:
    #final = final.upper()
    val1 = str(value1)
    finals = str(final)
    print (finals[0:],'------')
    #print (finals)
    val2 = val1.index('a')
    value1 = lists[0].upper()
    print (type(value1))
    value2 = lists[1].upper()
    
    print (val1)
    print (value1.split(' '))
    for i in value2[1:]:
        print (' '*4+"{}".format(i))
