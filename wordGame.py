#Maria Suarez
#MAke a word game with 3 different lists.
import os, random
os.system('cls')

# you must make a nice menu

Afruits=["banana", "apples", "Strawberries", "Blackberries", "mangos", 'oranges', 'kiwis']
for elem in Afruits:
    print(f"the fruit is {elem}")

for i in range(len(Afruits)-1):
    print(i, end=" ")
    print("The fruit is ",Afruits[i] )
# lenght=len(Afruits)-1
# indexFruit=random.randint(0,lenght)
# word=Afruits[indexFruit]
# print(word)
word=random.choice(Afruits) #picks one random element from the list
print(word)
guess=""
def guessFun():
    global guess
    check=True
    while check:
        try:
            guess = input("enter a guess ")
            if guess.isalpha():
                check=False
            else:
                print("Only letters please")
        except ValueError:
            print("Only letters please")
def playGame():
    global gameOn
    os.system('cls')
    answer=input("do you want to play again? ")
    if 'n' in answer.lower():
        gameOn=False
    else:
        print("playing again") #menu
gameOn=True
counter=0
letterGuessed=""
guessedLetter=0
while gameOn:
    #call guess function guessFun
    guessFun()
    letterGuessed +=guess#letterGuessed=letterGuessed +guess
    if guess not in word:
        counter +=1
        print(counter)
    for letter in word:
        # if guess in word:
        #     guessedLetter +=1
        #     print(guessedLetter)
        if letter in letterGuessed:
            print(letter, end=' ')
        else:
            print("_", end=" ")
            
    
    if counter >6:
        print("\nsorry too many guesses ")
        playGame()
    if guessedLetter == len(word):
        print ("\nyou won")
        playGame()
    
      



    # print(letter)
    # gameOn=False