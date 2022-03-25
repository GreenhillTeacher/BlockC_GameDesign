#MariaSuarez 
# 02/08/2022
import os, random
os.system('cls')
choice=0
def menu():
    print("## Word game with 3 levels  ##")
    print("##       1. Fruits          ##")   
    #        2. Animals 
    #        3. Computer Parts    
    # Choice:
    check=True
    
    while check:
        global choice
        try:
            choice=int(input("Enter your choice "))
            if choice>0 and choice<4:
                check = False
            else:
                print("enter a number from 1 to 3 only")
        except ValueError:
            print(" Please enter a number")

#Create word lists



word=""
guess=""
def selectWord():
    global word
    fruits=["bananas", "grapes", "waterMelon", 'blueberries', 'apples', "blackberries",
    "papaya", 'oranges', 'tomatoes', 'mangos', 'kiwis','strawberries' ]
    animals=["dog"]
    parts=["ram"]
    if choice ==1:
        word=random.choice(fruits)
    elif choice ==2:
        word=random.choice (animals)
    else:
        word = random.choice(parts)
    for letter in word:
        print("_", end=" ")
def guessFunction():
    global guess
    check=True
    while check:
        try:
            guess=input("\nenter a letter to guess the word ")
            if guess.isalpha() and len(guess)==1:
                check=False
            else:
                print("only one letter please")
        except ValueError:
            print("only one letter please")
def playAgain():
    global gameOn
    #ask user if they want to play again
    # if the anser is yes:
    #       clear, menu(),selectWord()highScore=0, 
    #       letterGuessed="",tries=0
    # else:
    #       clear screen print Thank you 
    #       your high score was ...print score
    #       gameOn=False         
gameOn=True
tries=0
letterGuessed=""
menu()
print(choice)
selectWord()
print()
highScore=0
while gameOn:
    
    guessFunction()
    letterGuessed += guess  #letterGuessed=letterGuessed + guess
    if guess not in word:
        tries +=1
        print(tries)# for testing delete when game is ready
    countLetter=0
    for letter in word:
        if letter in letterGuessed:
            print(letter, end=" ")
            countLetter +=1
        else:
            print("_", end=" ")
    if tries >6:
        print("\n Sorry run out chances ")
        playAgain() #ask if they want to play again
    if countLetter == len(word):
        print ("\nyou guessed! ")
        score= len(word)*5-2*tries
        if score > highScore:
            highScore= score
        playAgain()
    