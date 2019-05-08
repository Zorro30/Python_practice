'''
Your goal is to merge two dictionaries into one dictionary with two maximum values.
Dictionaries will be given line by line with their KeyValue pair, separated by a semicolon.
The output dictionary can have a single value linked to a key, which means the second value can be empty.

The display of the output dictionary content must be printed line by line, each line displaying a pair content as :
Key: Value1 and Value2
If the Value2 doesn't exist, then your program shouldn't print the " and Value2"

The display order of the printed pairs is the same order as pairs were read.
'''

#n1 = int(input())
w1 = dict()
w2 = dict()
for i in input().split():
    print(i)
    w1[i] = input()
#n2 = int(input())
for i in input().split():
    w2[i] = input()

print (w1.keys())