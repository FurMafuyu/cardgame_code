"""
Main file
"""
from cards import cards , collection
import copy

def main():
    collI = collection.init()
    if (collI != 0):
        print(str(collI) + " - Error while initializing collection")
        return -1


    matt = copy.deepcopy(collection.cardCollection[11])
    print(matt)
    print("Matthieu.takeDamage(4)")
    matt.takeDamage(4)
    print(matt)
    print("Matthieu.healthBoost(4)")
    matt.gainMaxHp(4)
    print(matt)
    print("Matthieu.heal(2)")
    matt.heal(2)
    print(matt)
    print("Matthieu.heal(25)")
    matt.heal(25)
    print(matt)

    return 0


if __name__ == "__main__" :
    main()