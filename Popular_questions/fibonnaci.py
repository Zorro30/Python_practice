

def feb(n):
    a, b = 0, 1
    series = []
    
    for i in range (n):
        series.append(a)
        a,b = b, a+b
    print (series)

n = int(input ("Enter the number till you want to find the series:"))

feb(n)


