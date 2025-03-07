from colorama import *
init(autoreset=True)

class Card:

    type = "init"
    name = "name_init"
    cost = 0

    def __init__(self, type, name, cost):
        self.type = type
        self.name = name
        self.cost = cost

    def __getattr__(self, name):
        if name == "type": #wat
            return self.type
        raise AttributeError(name)
    
    def __str__(self):
        return self.name + ", " + str(self.cost) + " Mana."


class Minion(Card):
    
    rawAtk = 0
    rawHp = 0
    atk = 0
    hp = 0

    def __init__(self, type, name, cost, atk, hp):
        super().__init__(type, name, cost)
        self.rawAtk = atk
        self.rawHp = hp
        self.hp = hp
        self.atk = atk
    
    def __str__(self):
        return self.name + ", " + str(self.cost) + " Mana, " + str(self.atk) + " | " + self.printHP()
    
    def takeDamage(self, amount):
        if amount >= self.hp:
            self.hp = 0
            print("AM DED,", self.name)
        else :
            self.hp = self.hp - amount

    def printHP(self):
        if self.hp < self.rawHp :
            return (Fore.RED + str(self.hp) + Fore.WHITE)
        elif self.hp > self.rawHp :
            return (Fore.GREEN + str(self.hp) + Fore.WHITE)
        else:
            return (str(self.hp))
