import random

while True:
    print("Welcome to Rock,paper,scissors")

    user_score = 0
    comp_score = 0
    ties = 0

    name = input("Enter your name here: ")

    print("""
    Winning Rules:

    1.Paper vs Rock --> Paper
    2.Paper vs Scissor --> Scissor
    3.Rock vs Scissor --> Rock
    """)

    choice =int(input("enter your choice from 1-3: "))
    print()

    while choice > 3 or choice < 1:
        choice = int(input("enter a valid output"))


    if choice == 1:
        user_choice = "Rock"
    elif choice == 2:
        user_choice = "Paper"
    else:
        user_choice = "Scissor"

    print("the user's choice is",user_choice)
    print("Now it's computer turn")

    computer = random.randint(1,3)

    if computer == 1:
        comp_choice = "Rock"

    elif computer == 2:
        comp_choice = "Paper"
    else:
        comp_choice = "Scissor"

    print("The computer choice is",comp_choice)

    if ((user_choice == "Rock" and comp_choice == "Paper") or (user_choice == "Paper" and comp_choice == "Rock")):
        print("paper wins")
        result = "paper"

    elif ((user_choice == "Rock" and comp_choice == "Scissor") or (user_choice == "Scissor" and comp_choice == "Rock")):
        print("rock wins")
        result = "rock"

    elif (user_choice == comp_choice):
        print("ties")
        result = "ties"

    else:
        print("Scissor wins")
        result = "Scissor"


    if result == "tie":
        tie +=1

    elif result == user_choice:
        print("user wins")
        user_score +=1

    else:
        print("computer wins")
        comp_score +=1


    print("scores are")    
    print(name, "'s score is",user_score)
    print("computer's score is",comp_score)

    repeat= input("do you want to play again? ")
    if repeat =="No" or repeat =="No":
        break

print("Game is over!!")
print("Thanks for playing!!")






