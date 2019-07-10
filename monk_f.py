import monk 

def monkey_f(self): 
    print ("monkey_f() is being called")
# replacing address of "func" with "monkey_f" 

monk.A.monk = monkey_f
obj = monk.A() 

obj.monk()