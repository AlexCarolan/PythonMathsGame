import random

difficulty = 4
diffCheck = 0
		
def game(gameNum):
	check = True
	global diffCheck
	global difficulty
	difficulty = 4
	diffCheck = 0
	score = 0
	while(check == True):
		#Generate the question values at random between 1 & the difficulty level		
		A = random.randint(1, difficulty)
		B = random.randint(1, difficulty)
		
		#If mixed choose random game
		if gameNum == 5:
			C = random.randint(1, 4)
		else :
			C = gameNum
		
		#Ensure the result is a positive int
		while((C == 2 and A - B < 0) or (C == 4 and A % B > 0)):
			A = random.randint(1, difficulty)
			B = random.randint(1, difficulty)
			
		#Calculate the result based on the type of calculation
		result = mixResult(A,B,C)
		
		#Output the question and verify the answer is a valid int
		inputValue = takeInput(A,B,C)
			
		#Verify that the input is the correct answer
		if inputValue == (result):
			if difficulty < 10:
				diffCheck += 1
			print("That is correct, well done!")
			score += difficulty
		else:
			print("\nNot right, the correct answer is:", result)
			if difficulty < 4:
				diffCheck -= 1

		#Adjust the difficulty level if required
		diffChange()
			
		#Check if the user would like to continue
		check = askExit()
	return score
	
def diffChange():
	global diffCheck
	global difficulty
	if diffCheck <= -3:
		if difficulty > 4:
			difficulty -= 1
		diffCheck = 0
	elif diffCheck >= 3:
		difficulty += 1
		diffCheck = 0
				
def mixResult(A,B,C):
	if C == 1:
		return A + B
	elif C == 2:
		return A - B
	elif C == 3:
		return A * B
	elif C == 4:
		return A / B

def askExit():
	while(True):
		userCheck = input("Press Y to try another sum or N to stop.\n")
		if userCheck in ('Y', 'y'):
			return True
		elif userCheck in ('N', 'n'):
			return False
			
def takeInput(A,B,C):
	map = {1 : "+", 2 : "-", 3 : "x", 4 : "/"}
	while(True):
		try:
			print("\nWhat is", A, map[C], B, "?")
			inputValue = int(input())
			return inputValue
		except ValueError:
			print("The provided input was not a number, please try agian!")
