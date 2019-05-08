class Parent():

    def print_last_name(self):
        print("Patel")

class Child(Parent):

    def print_first_name(self):
        print("Gaurang")

    def print_last_name(self):
        print("zindabad")

gau= Parent()

#gau.print_first_name()
gau.print_last_name()