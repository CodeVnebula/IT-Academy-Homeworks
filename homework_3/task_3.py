import random

symbol = random.randint(1, 4)

if symbol == 1:
    print("Clubs / ", end="", sep="")
elif symbol == 2:
    print("Diamonds / ", end="", sep="")
elif symbol == 3:
    print("Hearts / ", end="", sep="")
else:
    print("Spades / ", end="", sep="")

card = random.randint(1, 13)

if card == 1:
    print("2", end="", sep="")
elif card == 2:
    print("3", end="", sep="")
elif card == 3:
    print("4", end="", sep="")
elif card == 4:
    print("5", end="", sep="")
elif card == 5:
    print("6", end="", sep="")
elif card == 6:
    print("7", end="", sep="")
elif card == 7:
    print("8", end="", sep="")
elif card == 8:
    print("9", end="", sep="")
elif card == 9:
    print("10", end="", sep="")
elif card == 10:
    print("Jack", end="", sep="")
elif card == 11:
    print("Queen", end="", sep="")
elif card == 12:
    print("King", end="", sep="")
else:
    print("Ace", end="", sep="")
    