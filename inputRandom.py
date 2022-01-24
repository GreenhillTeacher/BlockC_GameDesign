import os
import random
os.system('cls')
#  --> is for comments
#Maria I SUarez
#01/20/2022
#
#learn user input
#LEarn other operators: %, ** , random numbers, branching
#Program asking the user to guess a number
#to clear the terminal

#Declare variables: and use input() function
userInfo=input("Enter a number between 5 and 15: ")
print(userInfo)
print(type(userInfo))
#typecasting
userInfo=int(userInfo)
print(userInfo+34)
print(userInfo/2)
print(userInfo%2) #modulus operator
if userInfo%2 == 0:
    print("The number is even!")
else:
    print("The number is odd")
#Create a random number
guess = random.randint(1,50)
print(guess)