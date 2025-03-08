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

    for e in collection.cardCollection:
        print(collection.cardCollection[e])

    """
    matt = copy.deepcopy(collection.cardCollection[11])
    print(matt)
    """


    return 0


if __name__ == "__main__" :
    main()