class Creature():
    "Basic Creature class with no type and default stats"
    def __init__(self, name, type = None):
        self.name = name
        self.type = type
        self.damage = 5
        self.hp = 10
        self.defense = 0

    def attack(self, creature):
        if not(creature.is_alive()):
            print("Cannot attack already dead creature ¯\\_(ツ)_/¯")
        else:
            real_damage = (self.damage - creature.defense)
            if(real_damage > creature.hp):
                real_damage = creature.hp
                creature.hp = 0
            else:
                creature.hp -= real_damage
            print("< {} attacked {} with {} damage ({} HP left (⋟﹏⋞) ) >".format(
                self.name, creature.name, real_damage, creature.hp
            ))
            if not(creature.is_alive()):
                print("< {} has died ✝>".format(creature.name))
        

    def is_alive(self):
        return (self.hp > 0)

    def __str__(self):
        if(self.is_alive()):
            return ("----------------------\n| Name: {}\n| Type: {}  \n|\n| Damage: {}\n| Defense: {}\n| HP: {}".format(self.name, self.type, self.damage, self.defense, self.hp))
        else:
            return ("Creature {} is dead ✝".format(self.name))

    def heal(self):
        self.hp += 2

class Fire_Creature(Creature):
    "Fire: higher attack, lower HP, no defense"
    def __init__(self, name, type = None):
        super().__init__(name, "Fire")
        self.damage = 9

class Water_Creature(Creature):
    "Water: higher defense, medium attack and HP"
    def __init__(self, name, type = None):
        super().__init__(name, "Water")
        self.defense = 5


class Earth_Creature(Creature):
    "Earth: high HP and can heal larger portion of HP"
    def __init__(self, name, type = None):
        super().__init__(name, "Earth")
        self.hp = 20
    
    def heal(self):
        self.hp += 10

first = Fire_Creature("Dragon")
second = Earth_Creature("Chicken")
third = Water_Creature("Dolphin")

print(first)
print(second)

second.attack(first)

print(third)

first.attack(second)
first.attack(second)
first.attack(second)
first.attack(second)

# TODO: start a loop and ask player to choose which creature to create, then let him choose which creature to attack