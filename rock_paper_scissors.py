#import random module
import random

#print the multiline instructions
#perform string concatenation of string

print("Winning Rules of the Rock paper scissor game as follows: \n"
+"Rock vs paper->Paper wins \n"+"Rock vs scissor->Rock wins \n"+"Scissor vs paper->Scissor wins")

while True:
    print("Enter choice \n 1.Rock \n 2.paper \n 3.Scissor \n")

    #take the input from the user
    choice = int(input("User turn: "))

    #OR is the short-circuit operator
    #if any one of the condition is true
    #then it return True value

    #looping until user enter invalid input
    while choice > 3 or choice <1: 
        choice = int(input("Enter valid input: "))
    
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissor'
    
    #print user choice
    
    #computer chooses randomly any number

    comp_choice = random.randint(1,3)

    #looping until comp_choice is equal to choice vavlue
    while comp_choice == choice :
        comp_choice = random.randint(1,3)

    #initialize the value of comp_choice_name
    if comp_choice == 1:
        comp_choice_name ='Rock'
    elif comp_choice == 2:
        comp_choice_name ='Paper'
    elif comp_choice == 3:
        comp_choice_name ='Scissors'

    print("Computer choice is:"+ comp_choice_name)
    
    print(choice_name + "V/s" + comp_choice_name)

    if((choice == 1 and comp_choice ==2 ) or (choice == 2 and comp_choice == 1)):
        print("paper wins => ", end ="")
        result = "Paper"
    elif((choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1)):
        print("Rock wins =>",end ="")
        result = "Rock"
    else:
        print("Scrissor wins =>", end ="")
        result = "Scissor"
    
    #Printing either user or computer wins
    if result == choice_name:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")

    print("Do you want to play again? (Y/N)")
    ans = input()

    #if user input n or N then condition is True
    if ans == 'n' or ans == 'N':
        break
    
    #after coming out of the while loop
    #we print thanks for playing

    

