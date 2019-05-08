import math
y = int(input("Enter the year you want to know the century:"))
if y == 0:
    print ("INVALID")
elif y>0:
    c = 1 + y//100
    if c%10==1: print ("{}st century CE".format(c))
    elif c%10==2: print ("{}nd century CE".format(c))
    elif c%10==3: print ("{}rd century CE".format(c))
    else: print ("{}th century CE".format(c))
elif y<0:
    c = -1*(y//100)
    print (c)
    if c%10==1: print ("{}st century BCE".format(c))
    elif c%10==2: print ("{}nd century BCE".format(c))
    elif c%10==3: print ("{}rd century BCE".format(c))
    else: print ("{}th century BCE".format(c))
