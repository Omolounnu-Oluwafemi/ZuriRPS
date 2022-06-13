import random

while True:
    playerChoice = input(
        "Make a Choice between \n P for Paper \n R for Rock and \n S for Scissors \n \n")

    playerChoice = playerChoice.lower()

    if playerChoice == "r":
        playerChoice = "Rock"
    elif playerChoice == "s":
        playerChoice = "Scissors"
    elif playerChoice == "p":
        playerChoice = "Paper"

    possibleChoice = ["Rock", "Paper", "Scissors"]
    computerChoice = random.choice(possibleChoice)

    if playerChoice in possibleChoice:
        print(
            f"\n Player {playerChoice} : CPU {computerChoice} \n")
        if playerChoice == "Paper" and computerChoice == "Rock":
            print("\n You are the Winner \n")
            break
        elif playerChoice == "Paper" and computerChoice == "Scissors":
            print("\n Computer is the Winner \n")
            break
        elif playerChoice == "Rock" and computerChoice == "Paper":
            print("\n Computer is the Winner \n")
            break
        elif playerChoice == "Rock" and computerChoice == "Scissors":
            print("\n You are the Winner \n")
            break
        elif playerChoice == "Scissors" and computerChoice == "Rock":
            print("\n Computer is the Winner \n")
            break
        elif playerChoice == "Scissors" and computerChoice == "Paper":
            print("\n You are the Winner \n")
            break
        else:
            print("It is a tie \n \n \n")

    else:
        print("Please choose between the correct Data")