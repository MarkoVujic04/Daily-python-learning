import random

computerChoice = random.choice("rps")
while True:
    userChoice = input("Rock, paper, scissors? (r/p/s): ").lower()
    if userChoice != "r" and userChoice != "p" and userChoice != "s":
        print("Not valid")
        continue
    elif userChoice == computerChoice:
        print("Draw, go again")
        computerChoice = random.choice("rps")
        continue
    elif userChoice == "r" and computerChoice != "p":
        print("You win")
        break
    elif userChoice == "p" and computerChoice != "s":
        print("You win")
        break
    elif userChoice == "s" and computerChoice != "r":
        print("You win")
        break
    else:
        print("You lose try again")
        continue