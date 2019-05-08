#print 1-10 without printing '5'. With use of continue and while

x = 1
while x!=11:
    if x == 5:
        x+=1
        continue
    print(x)
    x+=1
    