"""
Card classes creation file
"""

from colorama import *
init(autoreset=True)
from enum import Enum

class Rarity(Enum):
    COMMON = 1
    RARE = 2
    EPIC = 3
    LEGENDARY = 4
    FABULOUS = 5
    HIDDEN = 6
    
def kill(card):
    return 0

def annihilate(card):
    return 0


    
class Card:
    rarity = Rarity
    types = []
    name = "name_init"
    cost = 0

    def __init__(self, types, name, cost):
        self.types = types.split()
        self.name = name
        self.cost = cost
    
    def __str__(self):
        return f"[Card] - {self.types}, {self.name}, {self.cost} Mana."
    


class Minion(Card):
    rawAtk = 0
    atk = 0

    rawHp = 0
    maxHp = 0
    hp = 0

    def __init__(self, types, name, cost, atk, hp):
        super().__init__(types, name, cost)
        self.rawAtk = atk
        self.rawHp = hp
        self.hp = hp
        self.maxHp = self.rawHp
        self.atk = atk
    
    def __str__(self):
        return f"[Minion] - {self.types}, {self.name}, {self.cost} Mana, {self.printATK()} | {self.printHP()}"
    
    def takeDamage(self, amount):
        self.hp = self.hp - amount
        if self.hp <= 0:
            print(f"{self.name} is dead!")

    def printHP(self):
        if (self.maxHp > self.rawHp) & (self.hp == self.maxHp):
            return (Fore.GREEN + str(self.hp) + Fore.WHITE)
        if self.hp < self.maxHp :
            return (Fore.RED + str(self.hp) + Fore.WHITE)
        else:
            return (str(self.hp))

    def printATK(self):
        if self.atk < self.rawAtk :
            return (Fore.RED + str(self.atk) + Fore.WHITE)
        elif self.atk > self.rawAtk :
            return (Fore.GREEN + str(self.atk) + Fore.WHITE)
        else:
            return (str(self.atk))

    def gainMaxHp(self, amount):
        self.maxHp += amount
    
    def heal(self, amount):
        self.hp = min(self.maxHp, self.hp + amount)
    

