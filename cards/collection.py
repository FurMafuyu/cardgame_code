"""
This file is meant to create and stock every card created
"""
from .cards import Minion, Rarity

cardCollection = {
    0: Minion(Rarity.HIDDEN, "Dev", "Training Dummy", 1, 0, 2)
}

def init():
    # Minion(str types, str name, int cost, int ATK, int HP)
    minions = [
        # VALUES
        ## Unobtainable
        Minion(Rarity.FABULOUS, "Bauteique", "Furmafu", 9, 9, 9),
        Minion(Rarity.FABULOUS, "Prudistere", "Erebus", 9, 9, 9),
        Minion(Rarity.FABULOUS, "Acephane", "TMTC Chat", 9, 9, 9),
        Minion(Rarity.FABULOUS, "Forceroce", "OurseBrutale", 9, 9, 9),
        Minion(Rarity.FABULOUS, "Orgueique", "Perroquet", 9, 9, 9),
        Minion(Rarity.FABULOUS, "", "Chieng", 9, 9, 9),
        Minion(Rarity.FABULOUS, "", "Renard", 9, 9, 9),
        Minion(Rarity.FABULOUS, "Verileth", "Dragon", 9, 9, 9),
        Minion(Rarity.FABULOUS, "Avakon", "Rat", 9, 9, 9),
        Minion(Rarity.FABULOUS, "", "Furmafu", 9, 9, 9),
        Minion(Rarity.FABULOUS, "", "Furmafu", 9, 9, 9),
        Minion(Rarity.FABULOUS, "", "Furmafu", 9, 9, 9),
        Minion(Rarity.FABULOUS, "", "Furmafu", 9, 9, 9),
        Minion(Rarity.FABULOUS, "Bauteique", "Femme Peacock", 9, 9, 9), #PTT LA femme 14 ?

        # LEGENDARIES
        Minion(Rarity.LEGENDARY, "Animaler Cat", "Mordecai de Grammont", 4, 4, 5),
        Minion(Rarity.LEGENDARY, "Animaler", "Matthieu de Grammont", 7, 5, 5),
        Minion(Rarity.LEGENDARY, "Animaler Cat", "Fantoccio de Grammont", 7, 5, 5),
        Minion(Rarity.LEGENDARY, "Animaler Cat", "Miausric de Grammont", 7, 5, 5),
        Minion(Rarity.LEGENDARY, "Human", "Sa Majesté Louis", 7, 5, 5),
        Minion(Rarity.LEGENDARY, "Animaler Dog", "Belfort de Tours", 7, 5, 5),
        Minion(Rarity.LEGENDARY, "Animaler", "Matthieu de Grammont", 7, 5, 5),

        # EPICS
        Minion(Rarity.EPIC, "Human", "Tom Averti", 5, 5, 4),

        # RARES
        Minion(Rarity.RARE, "Human", "Préposé au crottin", 4, 3, 3),

        # COMMONS
        Minion(Rarity.COMMON, "Human", "Jardinier recycleur", 2, 2, 1)

        # DEVS
        ## Unobtainable
    ]

    startId = 10
    for e in minions:
        cardCollection[startId] = e
        startId += 1

    return 0
