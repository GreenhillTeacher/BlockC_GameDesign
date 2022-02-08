#Maria Suarez
#Learn Strings and several functions of string
import os, random
os.system('cls')
schoolName="Greenhill School"
schoolName=schoolName.upper()
print(len(schoolName))
#LAst index is len-1
lastCharacter= len(schoolName)-1
print(schoolName)
if "g" in schoolName:
    print("There is a blank in the word")
letter= random.choice(schoolName)
print(letter)
gameOn=True
for i in range(len(schoolName)):
   
    if letter == schoolName[i]:
        print(letter, end=" ")
    else:
        print("_", end=" ")

print()
