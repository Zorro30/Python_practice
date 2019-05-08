class Details:

    def __init__(self,value):
        self.value = value

    @property               # using @property we can get values to print.
    def get_val(self):
        return self.value
    
    @get_val.setter         # using @def_name.setter we can set the value for the same func. But the function name should be the same.
    def get_val(self,value):
        self.value = value
        return self.value

v = Details(5)
print(v.get_val)
v.get_val = 55
print(v.get_val)