import random

#Game presentation
print ("Welcome to the guess the number game")
print ("Do you want to guess the number or do you want me to guess? \n 1. I'll guess the number \n 2. I want you to guess") #User chooses type of game
gameType = int(input())

#Game settings
maxNumber = int(input ("What's the maximum possible number you want to allow? ")) #Max number of the inverval numbers to guess
maxGuesses = int(input ("How many tries do you want? ")) #How many tries?

possibleNumbers = list(range(1,maxNumber+1,1)) #Sets variable to list of possibilities for AI (Gametype 2)2
aiNumberPick = random.randrange(1,maxNumber) #Sets first number to try (Gametype 2)
intervalPossible = random.randrange(1,maxNumber) #Sets interval AI will try (Gametype 2)


if gameType == 1:
    secretNumber = random.randint(1, maxNumber)
    for guessesTaken in range (1, maxGuesses+1):
        print ("Take a guess")
        guess = int(input())
        if guess <secretNumber:
            print ("Too low")
        elif guess > secretNumber:
            print ("Too high")
        else:
            break
    if guess == secretNumber:
        print("You got it! In", str(guessesTaken), "tries")
    else:
        print("Sorry. Maximium tries reached. (", str(guessesTaken), ")")
elif gameType == 2:
    secretNumber = int(input("Enter the secret number: "))
    for guessesTaken in range(1, maxGuesses + 1):
        guess = aiNumberPick
        print("I'm thinking of..", guess)
        if guess < secretNumber:
            print("Oops! Too low")
            possibleNumbers = possibleNumbers[possibleNumbers.index(guess) + 1:]
            print ("I have the remaining numbers to pick", possibleNumbers)
        elif guess > secretNumber:
            print("Oops! Too high")
            possibleNumbers = possibleNumbers[:possibleNumbers.index(guess)]
            print ("I have the remaining numbers to pick", possibleNumbers)
        else:
            break
        if len(possibleNumbers) == 0:
            break
        aiNumberPick = random.choice(possibleNumbers)
    if guess == secretNumber:
        print("I got it! In", str(guessesTaken), "tries")
    else:
        print("Ops, you won. Maximum tries reached. The correct number was", secretNumber)