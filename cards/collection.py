"""
This file is meant to create and stock every card created
"""
from .cards import Minion, Rarity

cardCollection = {
    0: Minion(Rarity.HIDDEN, "Dev", "Training Dummy", 1, 2, 2)
}

def init():
    # Minion(str types, str name, int cost, int ATK, int HP)
    minions = [
        Minion(Rarity.LEGENDARY, "Animaler Cat", "Mordecai de Grammont", 4, 4, 5),
        Minion(Rarity.LEGENDARY, "Animaler", "Matthieu de Grammont", 7, 5, 5),
        Minion(Rarity.FABULOUS, "", "Furmafuyu", 9, 9, 9),
        Minion(Rarity.EPIC, "Human", "TKHTank", 5, 5, 4)
    ]

    startId = 10
    for e in minions:
        cardCollection[startId] = e
        startId += 1

    return 0