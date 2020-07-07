class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self, food):
        print("{}: Omnomnom, I like {}!".format(self.name, food))

class Doggo(Animal):
    def make_sound(self):
        print("{}: Woof!".format(self.name))
    
    def pet(self):
        print("{} is a good boy!".format(self.name))

class Monkey(Animal):
    def make_sound(self):
        print("{}: U u u a a a!".format(self.name))

    def swing(self):
        print("<{} swings on a wine. Weeee!>".format(self.name))

class Cate(Animal):
    def make_sound(self):
        print("{}: hear me roar! =^.^=".format(self.name))

    def eat(self, food):
        print("<{} looks at {} carefully>".format(self.name, food))
        super().eat(food)


animals = [Cate("Micka"), Doggo("Azorek")]

for animal in animals:
    animal.make_sound()
    animal.eat("meat")

goodBoy = Doggo("Good Boy")
ape = Monkey("MonkaS")
kitty = Cate("Kitty")

goodBoy.make_sound()
goodBoy.eat("Meat")
goodBoy.pet()

ape.make_sound()
ape.eat("Banana")
ape.swing()

kitty.make_sound()
kitty.eat("Tuna")