import random
from Games import addition, subtraction, multiplication, division

#Take and store the inital user selection input
inputNumber = input("Select one of the following options:\n(1) Addition (2) Subtraction (3) Multiplication (4) Division (5) Random sums (6) Quit\n")

#Run the game while the exit command has not been selected, also handles unexpected inputs
while (inputNumber != '6'):

	#Run the game selected by the user
	#ADDITION
	if inputNumber == '1':
		addition()
	#SUBTRACTION
	elif inputNumber == '2':
		subtraction()
	#MULTIPLICATION
	elif inputNumber == '3':
		multiplication()
	#DIVISION
	elif inputNumber == '4':
		division()
	#MIXTURE
	elif inputNumber == '5':
		print("Five!")
	#INVALID INPUT
	else:
		print("\nThe provided input was not valid, please try again!\n")
	
	#Take another user input to select a new game or exit the loop and terminate
	inputNumber = input("Select one of the following options:\n(1) Addition (2) Subtraction (3) Multiplication (4) Division (5) Random sums (6) Quit\n")

print("\nYou have chosen to quit, Good Bye!")
