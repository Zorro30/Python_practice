class Employee():
    amount_raise = 1.10
    def __init__(self,name,last_name,salary):
        self.name = name
        self.last_name = last_name
        self.salary = salary
        self.email = "{}.{}@email.com".format(name,last_name)
    
    def full_name(self):
        return "{} {}".format(self.name,self.last_name)

    def apply_raise(self):
        self.salary =  int(self.salary * self.amount_raise)

class Developer(Employee):
    amount_raise = 1.04

    def __init__(self,name,last_name, salary, prog_lang):
        super().__init__(name,last_name,salary)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self,name,last_name,salary,list_employees = None):
        super().__init__(name,last_name,salary)
        if list_employees is None:
            self.list_employees = []
        else:
            self.list_employees = list_employees

    def add_emp(self,emp):
        if emp not in self.list_employees:
            self.list_employees.append(emp)
    
    def remove_emp(self,emp):
        if emp in self.list_employees:
            self.list_employees.remove(emp)

    def show_emp(self):
        for emp in self.list_employees:
            print('-->', emp.full_name())


emp1 = Employee('Gaurang','Patel',26000)
emp2 = Developer('Bharat','Patel',50000,'python')

mgr1 = Manager('Gau','Patel',90000,[emp1])
emp1.apply_raise()
print(emp1.salary)
emp2.apply_raise()
print(emp2.prog_lang)
print(mgr1.email)

mgr1.add_emp(emp2)
mgr1.show_emp()
mgr1.remove_emp(emp2)
mgr1.show_emp()
