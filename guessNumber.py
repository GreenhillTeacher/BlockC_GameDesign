#import anything you need
# name
#date

#Showing the kids how to change a program in github

#What is the program about 
import os, random
os.system('cls')
print("#############################")
print("#   Guess a number Menu     #")
#ADD a MEnu

# choices  1-10
# choices 1 -50
# choices 1-100

#Select your choice



gameOn=True

#looping with condition
# #get the guess number from random
guess=random.randint(1,50)
guess2=random.ran
counter=0
while gameOn:
    userNum=input("Guess a number from 1 to 50 ")
    #check if the user guessed the number
    userNum=int(userNum)
    counter = counter+1
    if userNum == guess:
        print("You are so smart, you won!")
        gameOn=False
    else:
        if userNum > guess +10:
            print("too bad, you were too far up")
        else:
            if userNum < guess-10:
                print("too bad, you were too far low")
    if counter ==5:
        print("Sorry you did not guessed the number")
        gameOn=False
