#david l
#1/26/22
#rockpaperscissors with restart

import os
import random

os.system('cls')
gameOn = True
usrChoice = 0
compChoice = 0

#menu
def menu():
    global usrChoice
    checkNum = True
    print("*************************")
    print("Play Rock Paper Scissors!")
    print("*************************")
    print("      Enter  Choice      ")
    print("    Enter 1  For Rock    ")
    print("    Enter 2 For Paper    ")
    print("   Enter 3 For Scissors  ")
    print("*************************")
    #input validation
    print("\nChoice Here:", end = " ")
    while checkNum:
        usrChoice = input()
        try:
            usrChoice = int(usrChoice)
            if usrChoice < 4 and usrChoice > 0:
                checkNum = False
            else:
                print("Please enter a number between 1 and 3")
        except ValueError:
            print("That is not a valid input, Please try again")

#PLay again?
def replay():
    global gameOn
    print("Do you want to rematch?\n")
    print("Please enter 1 for yes or 2 for no")
    #input val
    rematchVal = True
    while rematchVal:
        rematch = input()
        try:
            rematch = int(rematch)
            if rematch < 3 and rematch > 0:
                rematchVal = False
            else:
                print("Please enter 1 for yes or 2 for no")
        except ValueError:
            print("That is not a valid input, Please try again")
    if rematch == 1:
        os.system('cls')
    if rematch == 2:
        gameOn = False

#Game Start
while gameOn:
    #call menu
    menu()

    #clr 
    os.system('cls')

    #print usr choice
    if usrChoice == 1:
        print("You Chose Rock \n")
    if usrChoice == 2:
        print("You Chose Paper \n")
    if usrChoice == 3:
        print("You Chose Scissors \n")

    #comp select and print
    compChoice = random.randint(1, 3)
    if compChoice == 1:
        print("Computer Chose Rock \n")
    if compChoice == 2:
        print("Computer Chose Paper \n")
    if compChoice == 3:
        print("Computer Chose Scissors \n")    
    
    #whjo won?
    if usrChoice == compChoice:
        print("You Tied!")
        replay() #call replay
    if usrChoice == 1 and compChoice == 2:
        print("You Lost sucker")
        replay()
    if usrChoice == 1 and compChoice == 3:
        print("You Won!")
        replay()
    if usrChoice == 2 and compChoice == 1:
        print("You Won!")
        replay()
    if usrChoice == 2 and compChoice == 3:
        print("You Lost sucker")
        replay()
    if usrChoice == 3 and compChoice == 1:
        print("You Lost sucker")
        replay()
    if usrChoice == 3 and compChoice == 2:
        print("You Won!")
        replay()
 