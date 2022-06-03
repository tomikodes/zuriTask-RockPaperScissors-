from pprint import pprint
import random

# possible options to choose from 
possibleOpt = ["R", "P", "S"]
computerOpt = random.choice(possibleOpt)
print("Welcome to Python Rock, Paper and Scissor game")
print("R is for Rock\nS is for scissor\nP is for Paper")



# function for player to play 
def userSelection():
    userInput = input(f"Select an option between \"R\" \"P\" \"S\" \n")
    return userInput



def bigInput():
        # loop for right selection
    while True:
    
        inputSelection = userSelection()

        if inputSelection == possibleOpt[0]:
            
            break
        elif inputSelection == possibleOpt[1]:
            
            break
        elif inputSelection == possibleOpt[-1]:
            
            break
        else:
            print('Wrong choice')
            continue
    return inputSelection

askUser = bigInput()



# function when player select rock 
def rInput():
     if computerOpt == "R":
         print("It's a tie, you chose the same option as the computer")
     elif computerOpt == "S":
         print("Rock smashes scissors, you win")
     else:
        print("Paper covers Rock, you lose")

# function when player select paper 
def pInput():
    if computerOpt == "P":
        print("It's a tie, you chose the same option as the computer")
    elif computerOpt =="R":
        print("Papper cover Rock, you win!")
    else:
        print("Scissors cut Paper, you lose")

# function when player select scissors
def sInput():
    if computerOpt == "S":
        print("It's a tie, you chose the same option as the computer")
    elif computerOpt == "P":
        print("Scissors cut Paper, you win")
    else:
        print("Rock smashes Scissors, you lose")


if askUser == "R":
    print(f"Player: R\nCPU: {computerOpt}")
    rInput()
elif askUser == "S":
    print(f"Player: S \nCPU: {computerOpt}")
    sInput()
else:
    print(f"Player: P\nCPU: {computerOpt}")
    pInput()
