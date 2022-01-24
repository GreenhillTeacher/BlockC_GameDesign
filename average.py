import os
#  --> is for comments
#Maria I SUarez
#01/18/2022
#
#Declare Variables, print values, 
#LEarn about operators, type of data
#Program to calculate the average of 3 tests
os.system('cls')  #to clear the terminal
#Declare variables:
test1=89
test2=78
test3=91.5
Flag=True
#to display results we use print()
print(type(Flag))  #display type of data
#Calculate sum of tests
sum = test1 + test2 + test3
#Calculate average
#print statemnts authomatically add a return at the end of the print
print("This is the average of the 3 tests ", end='=')
average= int((sum/3)*100) #type casting
print(average/100)
print ("The average of "+ str(test1) + ", " + str(test2)+ ", and "+str(test3) + " is ", end='=') 
print(average/100)
print(15//2)
#exponent
print(2**3)
