#Please write a program which count and print the numbers of each character in a string input by console.
'''abcdefgabc
Then, the output of the program should be:

a,2
c,2
b,2
e,1
d,1
g,1
f,1
'''

store = dict()
s = input("Enter the string:") 
for i in s:
    store [i] = store.get(i,0)+1
    
print (store)