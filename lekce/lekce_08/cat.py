class Cat:
    def __init__(self, name):
        self.hp = 9
        self.name = name

    def __str__(self):
        return '<Cat {} has {} HP>'.format(self.name, self.hp)

    def meow(self):
        print("{}: Meow...  =^.^=".format(self.name))

    # def is_alive(self):
    #     if(self.hp > 0):
    #         #print("CAT IS ALIVE")
    #         return True
    #     else:
    #         #print("CAT IS ALIVE")
    #         return False
    def is_alive(self):
        return self.hp > 0

    def lose_life(self):
        if(self.is_alive()):
            self.hp -= 1
            print("*sad kitten noises* HP-1")
        else:
            print("Cat is already DEAD, nothing can hurt it now")

    def eat(self, food):
        if (food == "fish"):
            if (self.is_alive()):
                if (self.hp < 9 ):
                    print("Omnomnom tasty fish HP+1")
                    self.hp += 1
                else:
                    print("Cat is full!")
            else:
                print("Cat is already DEAD, she is the food now")
        else:
            print("You didn't give me fish!")

cat = Cat("Garfield")
cat.is_alive()
print(cat)
cat.eat("fish")
print(cat)
cat.lose_life()
print(cat)
cat.eat("fish")
print(cat)
cat.lose_life()
cat.lose_life()
cat.lose_life()
cat.lose_life()
cat.lose_life()
cat.lose_life()
cat.lose_life()
cat.lose_life()
cat.lose_life()
cat.lose_life()
cat.lose_life()
print(cat)
cat.eat("fish")

print(cat.__dict__)