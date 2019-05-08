class Mario():

    def move(self):
        print("I am flying!")

class SuperMario():

    def move_in(self):
        print("I am travelling!")

class BigMario(Mario,SuperMario):
    pass

gau = BigMario()

gau.move()
gau.move_in()