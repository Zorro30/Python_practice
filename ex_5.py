""" '''
reverse a string without reversing the special characters.
eg: 
input: abc$d%e
output: edc$b%a
'''

n = input()
pos = dict()
new = list()
final = list()
for i in range(len(n)):
    if n[i].isalnum():
        new.append(n[i])
    else:
        pos[i] = n[i]
new = new[::-1]
j = 0
for i in range(len(n)):
    if i in pos.keys():
        final.append(pos[i])
    else:
        if len(new) == 0:
            pass            
        else:
            final.append(new[j])
        j+=1
print(''.join(str(i) for i in final))
 """
import matplotlib.pyplot as plt
import numpy as np
plt.ion() ## Note this correction
fig=plt.figure()
plt.axis([0,1000,0,1])

i=0
x=list()
y=list()

while i <1000:
    temp_y=np.random.random();
    x.append(i);
    y.append(temp_y);
    plt.scatter(i,temp_y);
    i+=1;
    plt.show()
    plt.pause(0.0001)