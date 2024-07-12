import random

class Pokemon:

    def __init__(self, name, health, element):
        self.name = name
        self.health = health
        self.element = element

    def doMove(self): #this features that all pokemon can do
        print("Pokemon Move")

    def doEat(self):
        print("Pokemon Eat")


class JigglyPuff(Pokemon):
    def __init__(self, name, health, element, lungCapacity): # color is the unique feature that the jigglypuff has
        super().__init__(name, health, element)
        self.lungCapacity = lungCapacity #this will only show for jigglypuff

    def doMove(self):# to overwrite the general doMove in Pokemon
        super().doMove()
        print("JigglyPuff can float")
    
    def __str__(self):
        return f"Name: {self.name}\nHealth: {self.health}\nElement: {self.element}\nLungcapacity: {self.lungCapacity}"
    

class Pikachu(Pokemon):
    def __init__(self, name, health , element, electricity):
        super().__init__(name, health, element)
        self.electricity = electricity

    def __str__(self):
       return f"Name: {self.name}\nHealth: {self.health}\nElement: {self.element}\nElectricity: {self.electricity}" 

# class SuperPower:
#     def __init__(self):
#         pass

#     def __str__(self):
#         pass
# class Thunderbolt(SuperPower):
#     def __init__(self):
#         super().__init__()

# class Fireball(SuperPower):
#     def __init__(self):
#         super().__init__()

class Game:
    def __init__(self):
        self.element = ["thunder","fire","water","ghost","ghost","ice"]
        self.pokemon = {
            "JigglyPuff" :[JigglyPuff(f"J{i}", random.randint(50, 100), self.element[random.randint(0, len(self.element) - 1)], random.randint(50, 100)) for i in range(0, random.randint(3, 15))],
            "Pikachu" :[Pikachu (f"P{i}", random.randint(50,100), self.element[random.randint(0, len(self.element)-1)],random.randint(50,100)) for i in range(0, random.randint(5,20))]
            
        }
    def __str__(self):
        message = ""
    
        for pokemonname, pokemonlist in self.pokemon.items():
            for pokemon in pokemonlist:

                message += pokemon.__str__() + "\n" + ("-" * 20) + "\n"
        return message
    

game = Game()
print(game)