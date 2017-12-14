from Games import game

#Take and store the inital user selection input
inputNumber = input("Select one of the following options:\n(0) Scores (1) Addition (2) Subtraction (3) Multiplication (4) Division (5) Random sums (6) Quit\n")
score = 0
addScore = 0
subScore = 0
mulScore = 0
divScore = 0
mixScore = 0

#Run the game while the exit command has not been selected, also handles unexpected inputs
while (inputNumber != '6'):

	#Run the game or command selected by the user
	if inputNumber == '0':
		print("SCORES\nAddition:\t", addScore, "\nSubtraction:\t", subScore, "\nMultiplication:\t", mulScore, "\nDivision:\t", divScore, "\nRandom Sums:\t", mixScore, "\n")
	#ADDITION
	elif inputNumber == '1':
		result = game(1)
		score += result
		addScore += result
	#SUBTRACTION
	elif inputNumber == '2':
		result = game(2)
		score += result
		subScore += result
	#MULTIPLICATION
	elif inputNumber == '3':
		result = game(3)
		score += result
		mulScore += result
	#DIVISION
	elif inputNumber == '4':
		result = game(4)
		score += result
		divScore += result
	#MIXTURE
	elif inputNumber == '5':
		result = game(5)
		score += result
		mixScore += result
	#INVALID INPUT
	else:
		print("\nThe provided input was not valid, please try again!\n")
	
	#Take another user input to select a new game or exit the loop and terminate
	print("Total Score:", score, "- Select one of the following options:\n(0) Scores (1) Addition (2) Subtraction (3) Multiplication (4) Division (5) Random sums (6) Quit\n")
	inputNumber = input()

print("\nYou have chosen to quit, Good Bye!")
