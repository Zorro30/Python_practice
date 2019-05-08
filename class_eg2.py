class Enemy:

    def __init__(self, energy):
        self.energy = energy

    def get_energy(self):
        print (self.energy)

jason = Enemy(5)
gaurang= Enemy(15)

jason.get_energy()
gaurang.get_energy()