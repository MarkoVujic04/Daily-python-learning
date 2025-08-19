import random

randomNumber = random.randint(1, 100)
while True:
    userGuess = int(input("Guess the number between 1 and 100: "))
    if userGuess < 1 or userGuess > 100:
        print("Try again")
        continue
    elif userGuess == randomNumber:
        print("Congrats")
        break
    else:
        if userGuess < randomNumber:
            print("Too low")
            continue
        else:
            print("Too high")
            continue



