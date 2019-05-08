'''
A word ladder is a sequence of words of the same length where each word in the sequence changes exactly one 
letter in the previous word. Here's an example of a word ladder connecting "mate" and "vial":

mate
mite
mile
mill
dill
dial
vial

Given the terms of an attempted word ladder, determine whether it is valid. 
That is, all the words should be the same length, and each step should result from changing exactly one letter. Also, there should be no duplicates among the words, and there should be at least 2 words.

Input
7
mate
mite
mile
mill
dill
dial
vial

Output
true
'''
total = list()
check = False
prev = ''

n = int(input())
for i in range(n):
    one = input()
    total.append(one)
print(total)
for i in range(len(total)-1):
    if total[i] == total[i+1]:
        check = False
    elif len(total[i]) != len(total[i+1]):
        check = False
    else:
        count = 0
        for j in total[i]:
            for m in total[i+1]:
                if m == j:
                    count +=1
                    if count == len(total[i]) - 1:
                        check = True    
                    else:
                        check = False
            # if j not in prev and count ==0:
            #     check = True
            #     prev = total[i]
            #     count +=1
            #     break
            # else:
            #     check = False
if check:
    print('true')
else:
    print('false')
    