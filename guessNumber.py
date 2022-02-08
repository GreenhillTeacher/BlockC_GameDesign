#import anything you need
# name
#date

#Showing the kids how to change a program in github

#What is the program about 

#Finish the game by changing the number of tries in each level 
#and change the hints for each level 


import os, random
os.system('cls')
<<<<<<< HEAD
def menu(): #make a better menu
    print ("                                      ")
    print("*****************************")
    print("    *Guess a number menu*    ")
    print("*****************************")
    print("                             ")

    print("*        [1] 1-10         *")
    print("         [2] 1-50")
    print("         [3] 1-100")
#fix the MEnu
=======
print("#############################")
print("#   Guess a number Menu     #")
print("#                           #")
print("#      1. guess 1-10        #")
#ADD a MEnu
>>>>>>> 2fc7a433cc3470006447097b0d6f9b15a77ce0b7

# choices  1-10
# choices 1 -50
# choices 1-100

#Select your choice
<<<<<<< HEAD
#DECLARE ALL VARIABLES1
#How do we ask the user for choice
guess=0# by declaring the variable here is global variable
level=0
gameType=''

#check for the right input
# try/except
menu()  #calling the menu function
check=True
while check:
    gameType=input("Please select a level of the game ")
    #input always returns a string
    try:
        gameType=int(gameType)
        if gameType >0 and gameType<4:
            check=False
        else:
            print("\nPlease enter a number between 1 and 3")
    except ValueError:
        print("Sorry, wrong input try again")

def randomNum(gameType):
    global level
    global guess
    if gameType== 1:
        guess=random.randint(1,10)  #local variable
        level=10
    if gameType==2:
        guess=random.randint(1,50)  #local variable
        level=50
    if gameType==3:
        guess=random.randint(1,100)  #local variable
        level=100

randomNum(gameType) #this is the call of the function
finish=False
gameOn=True #VAriable to control loop
counter=0
answer=" "
while gameOn:
    message="Guess a number from 1 to "+ str(level)+" "
    userNum=input(message)
=======
#try and except
#add a loop so that the user can try again
check = True
while check:
    try:
        choice= int(input("choice: "))
        if choice > 0 and choice <4:
            check = False
        print ("Please enter a number from 1 to 3")
    except ValueError:
        print ('Sorry, try again ')
        
#check what choice to create the random number

if choice ==1:
    guess=random.randint(1,10)
elif choice ==2:
    guess=random.randint(1,50)
else:
    guess=random.randint(1,100)
gameOn=True
#looping with condition
counter=0
print(guess)
while gameOn:
    userNum=input("Guess a number")# input always return a string
>>>>>>> 2fc7a433cc3470006447097b0d6f9b15a77ce0b7
    #check if the user guessed the number
    userNum=int(userNum)    #typr casting to integer
    counter = counter+1   #controlling how many guesses the user can have
    if userNum == guess:
        print("You are so smart, you won!")
        finish=True
    else:
        if userNum > guess +10:
            print("too bad, you were too far up")
        else:
            if userNum < guess-10:
                print("too bad, you were too far low")
    if counter ==5 and gameOn:
        print("Sorry you did not guessed the number")
<<<<<<< HEAD
        finish=True
    if finish:
        os.system('cls')
        answer= input("Would you like to play again? ")
        if 'y' or "Y"  in answer:
            
            menu()
            randomNum(gameType)
            finish=False
            counter=0
        if 'n' in answer:
            
            print("Thank you for palying!")
            gameOn=False
            finish=False
            
=======
        gameOn=False
>>>>>>> 2fc7a433cc3470006447097b0d6f9b15a77ce0b7
