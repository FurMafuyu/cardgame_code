from cards import cards  

def main():
    print("Hey")

    Test = cards.Card("WIP","Petit test",2)
    print(Test)
    Dummy = cards.Minion("Minion", "Training Dummy", 1, 2, 2)
    print(Dummy)
    Dummy.takeDamage(1)
    print(Dummy)
    Dummy.takeDamage(1)
    print(Dummy)


if __name__ == "__main__" :
    main()