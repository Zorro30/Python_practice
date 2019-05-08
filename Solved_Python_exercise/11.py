#Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.


class number(object):

    def __init__(self,n):
        self.n=n

    def divBySeven(self):
        for i in range (0,self.n):
            if i%7==0:
                yield i

for num in number(100).divBySeven():
    print (num)