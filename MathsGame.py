import random

#Take and store the inital user selection input
inputNumber = input("Select one of the following options:\n(1) Addition (2) Subtraction (3) Multiplication (4) Division (5) Random sums (6) Quit\n")

#Run the game while the exit command has not been selected, also handles unexpected inputs
while (inputNumber != '6'):
	
	#Reset the game values to their inital state
	difficulty = 4
	check = True
	
	#Run the game selected by the user
	#ADDITION
	if inputNumber == '1':
		while(check == True): 
			#Generate the question values at random between 1 & the difficulty level
			A = random.randint(1, difficulty)
			B = random.randint(1, difficulty)
			
			#Output the question and verify the input is a valid int
			inputCheck = False
			while(inputCheck == False):
				try:
					print("\nWhat is ", A, " + ", B, "?")
					inputValue = int(input())
					inputCheck = True
				except ValueError:
					print("The provided input was not a number, please try agian!")
				
			#Verify that the input is the correct answer
			#If so the increase the dificulty by 1 to max of 10
			if inputValue == (A + B):
				if difficulty < 10:
					difficulty += 1
				print("That is correct, well done!")
			else:
				print("\nNot right, the correct answer is:", (A+B))
			
			#Check if the user would like to continue - Loop back if yes - exit if no -
			while(True):
				userCheck = input("Press Y to try another sum or N to stop.\n")
				if userCheck in ('Y', 'y'):
					break
				elif userCheck in ('N', 'n'):
					check = False
					break
	#SUBTRACTION
	elif inputNumber == '2':
		while(check == True): 
			#Generate the question values at random between 1 & the difficulty level
			A = random.randint(1, difficulty)
			B = random.randint(1, difficulty)
			
			#Output the question and verify the answer is a valid int
			inputCheck = False
			while(inputCheck == False):
				try:
					print("\nWhat is ", A, " - ", B, "?")
					inputValue = int(input())
					inputCheck = True
				except ValueError:
					print("The provided input was not a number, please try agian!")
				
			#Verify that the input is the correct answer
			#If so the increase the dificulty by 1 to max of 10
			if inputValue == (A - B):
				if difficulty < 10:
					difficulty += 1
				print("That is correct, well done!")
			else:
				print("\nNot right, the correct answer is:", (A-B))
				
			#Check if the user would like to continue - Loop back if yes - exit if no -	
			while(True):
				userCheck = input("Press Y to try another sum or N to stop.\n")
				if userCheck in ('Y', 'y'):
					break
				elif userCheck in ('N', 'n'):
					check = False
					break
	#MULTIPLICATION
	elif inputNumber == '3':
		while(check == True):
			#Generate the question values at random between 1 & the difficulty level		
			A = random.randint(1, difficulty)
			B = random.randint(1, difficulty)
			
			#Output the question and verify the answer is a valid int
			inputCheck = False
			while(inputCheck == False):
				try:
					print("\nWhat is ", A, " x ", B, "?")
					inputValue = int(input())
					inputCheck = True
				except ValueError:
					print("The provided input was not a number, please try agian!")
				
			#Verify that the input is the correct answer
			#If so the increase the dificulty by 1 to max of 10
			if inputValue == (A * B):
				if difficulty < 10:
					difficulty += 1
				print("That is correct, well done!")
			else:
				print("\nNot right, the correct answer is:", (A*B))
				
			#Check if the user would like to continue - Loop back if yes - exit if no -
			while(True):
				userCheck = input("Press Y to try another sum or N to stop.\n")
				if userCheck in ('Y', 'y'):
					break
				elif userCheck in ('N', 'n'):
					check = False
					break
	#DIVISION
	elif inputNumber == '4':
		print("Four")
	#MIXTURE
	elif inputNumber == '5':
		print("Five!")
	#INVALID INPUT
	else:
		print("\nThe provided input was not valid, please try again!\n")
	
	#Take another user input to select a new game or exit the loop and terminate
	inputNumber = input("Select one of the following options:\n(1) Addition (2) Subtraction (3) Multiplication (4) Division (5) Random sums (6) Quit\n")

print("\nYou have chosen to quit, Good Bye!")