#import anything you need
# name
#date

#Showing the kids how to change a program in github

#What is the program about 
import os, random
os.system('cls')
print("#############################")
print("#   Guess a number Menu     #")
print("#                           #")
print("#      1. guess 1-10        #")
#ADD a MEnu

# choices  1-10
# choices 1 -50
# choices 1-100

#Select your choice
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
    #check if the user guessed the number
    userNum=int(userNum)    #typr casting to integer
    counter = counter+1   #controlling how many guesses the user can have
    if userNum == guess:
        print("You are so smart, you won!")
        gameOn=False
    else:
        if userNum > guess +10:
            print("too bad, you were too far up")
        else:
            if userNum < guess-10:
                print("too bad, you were too far low")
    if counter ==5 and gameOn:
        print("Sorry you did not guessed the number")
        gameOn=False
