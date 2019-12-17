class PartyAnimal:
    x = 0
    name = ""
    
    def __init__(self, z) :
        self.name = z
        print(self.name, "constructed")
        
    def party(self) :
        self.x = self.x + 1
        print(self.name , "party count" , self.x)

an = PartyAnimal("Sally")
an.party()
an.party()
an = 55
print('an contains',an)


class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)
        

o = FootballFan("Jim")
o.party()
o.touchdown()
print(o.name)
                