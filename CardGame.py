#Maria Suarez
#02/15/2022
# Lists and methods
#STart  a card game (WAR)
import os, random
os.system("cls")
numberCards=[]
for i in range(2, 11):  #last value is never included
    numberCards.append(i)
    numberCards[i-2]=str(numberCards[i-2])
print(numberCards)
suits=['♠','♣','♥','♦']
royals=['J','Q','K','A']
#append the royal cards to the card numbers

for j in range(4):
    numberCards.append(royals[j])

print(numberCards)
deck=[]
for suit in range(4):
    print(suits[suit])
    for card in range (13):
        cards= (numberCards[card] +" "+ suits[suit])
        #This makes each card, cycling through suits
        deck.append(cards)
        
print(deck)
random.shuffle(deck)
print (deck)

    
