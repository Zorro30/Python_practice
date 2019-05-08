class Enemy:
    
    lives= input("Please eneter the no. of lives you want to provide: ")
    life = int(lives)

    def attack(self):
        #while int(life) > 0:
        print("ouch!")
        self.life -=1
        """if life == 0:
            print ("Please start again!")
        exit"""

    def checklife(self):
        if self.life <= 0:
            print ("I am dead.")
        else:
            print(str(self.life) + " Life left")
    
    def getlife(self):
        if self.life < 4:
            print ("Don't worry I am here to save you!")
            self.life +=5
            print ("Now you have " + str(self.life) + " lives")
        else:
            print ("You already have sufficient life")

enemy1=Enemy()

enemy1.attack()
enemy1.attack()
enemy1.attack()
enemy1.attack()
enemy1.attack()
#enemy1.checklife()
enemy1.getlife()



