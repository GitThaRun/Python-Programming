import random

options = ("rock","paper","scissors")
running = True

while running:

    playerChoice = None
    ComputerChoice = random.choice(options)

    while playerChoice not in options:
        playerChoice = input("Enter Your Choice (rock/paper/scissors) : ").lower()

    print(f"PlayerChoice : {playerChoice}")
    print(f"Computer's Choice : {ComputerChoice}")

    if playerChoice == ComputerChoice:
        print("It's A Tie")
    elif playerChoice == "rock"  and ComputerChoice == "scissors":
        print("You Win!")
    elif playerChoice == "paper" and ComputerChoice == "rock":
        print("You Win!")
    elif playerChoice == "scissors" and ComputerChoice == "paper":
        print("You Win!")
    else:
        print("You Lose")

    if not input("PlayAgain?(Y/N) : ").upper() == "Y":
        running = False
print("Thanks For Playing!")