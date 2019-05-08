def nprimes(n):
    count = 0
    a_list = list()
    i = 1
    while count < n:
        if isprime(i):
            a_list.append(i)
            count +=1
        i += 1 
    print(a_list)


def isprime(n):

    if n > 1:
        for i in range(2,n):
            if n % i == 0:
                return False
        else:
            return True
            
nprimes(int(input('Enter the number of prime numbers you want:')))