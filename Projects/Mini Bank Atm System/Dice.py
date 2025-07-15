import random

# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘

# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

diceArt = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    
    2: ("┌─────────┐",
        "│ ●       │",
        "│         │",
        "│        ●│",
        "└─────────┘"),

    3 :("┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    
    4 :("┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"),
    
    5 :("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"),

    6 :("┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘")
}

dice = []
numOfDice = int(input("Enter Number Of Dice : "))

if numOfDice > 0:

    for die in range(numOfDice):
        dice.append(random.randint(1,6))
    print("Dice Rolled:", dice)

    for lines in range(5):
        for die in dice:
            print(diceArt.get(die)[lines],end = "")
        print()
else:
    if numOfDice < 0:
        print("Invalid! Value Should be Greater than One")
    else:
        print("At least One Die Should be Rolled!")