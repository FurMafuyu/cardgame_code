"""
This file is meant to create and stock every card created
"""
from .cards import Minion

cardCollection = {
    0: Minion("Dev", "Training Dummy", 1, 2, 2)
}

def init():
    # Minion(str types, str name, int cost, int ATK, int HP)
    minions = [
        Minion("Animaler Cat", "Mordecai de Grammont", 4, 4, 5),
        Minion("Animaler", "Matthieu de Grammont", 7, 5, 5),
        Minion("Human", "TKHTank", 5, 5, 4)
    ]

    startId = 10
    for e in minions:
        cardCollection[startId] = e
        startId += 1

    return 0