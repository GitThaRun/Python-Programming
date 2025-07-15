import random

start_value = 1
End_Value = 100

num = random.randint(start_value,End_Value)
isRunning = True
guesses = 0

print("WELCOME TO NUMBER GUESSING GAME : ")

while isRunning:
    
    userNum = (input(f"Guess a Number Between {start_value} and {End_Value} : "))
   

    if userNum.isdigit():
        userNum = int(userNum)
        guesses += 1

        if userNum < start_value or userNum > End_Value:
            print("Number is out of Range")
        elif userNum < num:
            print("TOo Low")
        elif userNum > num:
            print("Too High")
        else:
            print(f"You Guessed it!!The Number is {num}")
            print(f"You Took {guesses} guesses")
            isRunning = False

    else:
        print("Invalid!")
        print(f"select Number between {start_value} and {End_Value}!!")