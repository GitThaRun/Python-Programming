questions = ("1.What is the main gas responsible for the greenhouse effect on Earth?",
             "2.Who is known as the father of the computer?",
             "3.Which planet in our solar system has the most moons?",
             "4.What does 'HTTP' stand for in a website URL?",
             "5.Which part of the human brain is responsible for coordination and balance?")

options = (("A.Oxygen", "B.Nitrogen", "C.Carbon Dioxide", "D.Hydrogen"),
           ("A.Bill Gates", "B.Charles Babbage", "C.Alan Turing", "D.Elon Musk"),
           ("A.Earth", "B.Jupiter", "C.Mars", "D.Saturn"),
           ("A.HyperText Transfer Protocol", "B.High Tech Transmission Program","C.HyperText Transfer Page", "D.Hosting Text Transfer Page"),
           ("A.Cerebrum", "B.Medulla", "C.Cerebellum", "D.Hypothalamus"))

answers = ("C","B","D","A","C")

guesses = []
question_num = 0
score = 0

for q in questions:
    print("----------------")
    print(q)

    for option in options[question_num]:
        print(option)
    
    guess = (input("Enter Your Answer (A/B/C/D) : ")).upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"Correct Answer is {answers[question_num]}")
    question_num += 1

print("----------------")
print("Quiz Result")
print("----------------")

print("Answers : ",end = " ")
for answer in answers:
    print(answer,end = " ")
print()

print("Your Guesses : ",end = " ")
for guess in guesses:
    print(guess,end = " ")
print()

score = float(score/len(questions) * 100)
print(f"You Scored : {score : .2f}")