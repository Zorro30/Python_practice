"""
Recursion
1) factorial & 2)fibonnaci
3) Think of a recusive version of the function f(n) = 3 * n, i.e. the multiples of 3
4) Write a recursive Python function that returns the sum of the first n integers.
5) Write a function which implements the Pascal's triangle:

            1
          1     1
        1    2    1
      1    3    3    1
    1    4    6    4    1
  1    5    10    10    5    1

"""
# 1)
def factorial(n):
    print("factorial has been called with n = " + str(n))
    if n == 1:
        return 1
    else:
        res = n * factorial(n-1)
        print("intermediate result for ", n, " * factorial(" ,n-1, "): ",res)
        return res	

# print(factorial(5))

# 2)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
# print(fibonacci(10))

# 3)
def multiples(n):
    if n == 1:
        return 3
    else:
        return multiples(n-1)+3

# print(multiples(6))

# 4)
def sum_n_integers(n):
    
    if n == 1:
        return 1
    else:
        return sum_n_integers(n-1) + n

# print(sum_n_integers(5))

# 5)
def pascal(n):
    if n == 1:
        return [1]
    else:
        line = [1]
        previous_line = pascal(n-1)
        for i in range(len(previous_line)-1):
            line.append(previous_line[i] + previous_line[i+1])
        line += [1]
    return line

# print(pascal(6))