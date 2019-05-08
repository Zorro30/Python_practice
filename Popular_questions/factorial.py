def factorial(num):
    def fact(n):
        if n == 0:
            return 1
        else:
            return factorial(n-1) * n

    return fact(num)

print (factorial(4))