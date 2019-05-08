'''
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
eg. New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
OutPut:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
'''

freq = {}

line = input("Enter the sentence:")

for word in line.split(' '):
    freq[word] = freq.get(word,0)+1

words = list(freq.keys())
words.sort()


for w in words:
    print (w,freq[w])