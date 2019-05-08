class Employee:

    def __init__(self,first,last):
        self.first = first
        self.last = last

    @property   #here we are defining email as a method but using it as an attribute by using @property.
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)
    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    @fullname.setter
    def fullname(self,name):
        first , last = name.split(' ')
        self.first, self.last = first, last

emp1 = Employee('Gau','Patel')
emp1.fullname  = 'Gaurang Patel'
print(emp1.email)
print(emp1.fullname)
print(emp1.first)