class Kitten:
    def __init__(self, name):
        self.name = name
    # def meow(self):
    #     print("Meow...")
    def __str__(self):
        return '<Kitten named {}>'.format(self.name)
    def meow(self):
        print("{}: Meow...  =^.^=".format(self.name))

    def whoAmI(self):
        print("I'm {}, hear me roar!".format(self.name))

    def eat(self, food):
        print("{}: Thanks for the {}! :3".format(self.name, food))

mourek = Kitten("Mourek")
#mourek.name = "Mourek"

micka = Kitten("Micka")
#micka.name = "Micka"

print(mourek)

micka.whoAmI()
micka.meow()

mourek.whoAmI()
mourek.meow()

micka.eat("fish")
mourek.eat("tuna")
# print(mourek.name)
# print(micka.name)

# najednou se da prepsat cela funkce a pak nebude vubec fungovat
# micka.meow = 1234
# micka.meow()

