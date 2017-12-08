import random

def addition():
	check = True
	difficulty = 4
	diffCheck = 0
	while(check == True): 
		#Generate the question values at random between 1 & the difficulty level
		A = random.randint(1, difficulty)
		B = random.randint(1, difficulty)
		
		#Output the question and verify the input is a valid int
		inputCheck = False
		while(inputCheck == False):
			try:
				print("\nWhat is", A, "+", B, "?")
				inputValue = int(input())
				inputCheck = True
			except ValueError:
				print("The provided input was not a number, please try agian!")
			
		#Verify that the input is the correct answer
		if inputValue == (A + B):
			if difficulty < 10:
				diffCheck += 1
			print("That is correct, well done!")
		else:
			print("\nNot right, the correct answer is:", (A+B))
			if difficulty < 4:
				diffCheck -= 1
			
		#Adjust the difficulty level if required
		if diffCheck <= -3:
			if difficulty > 4:
				difficulty -= 1
			diffCheck = 0
		elif diffCheck >= 3:
			difficulty += 1
			diffCheck = 0
		
		#Check if the user would like to continue - Loop back if yes - exit if no -
		while(True):
			userCheck = input("Press Y to try another sum or N to stop.\n")
			if userCheck in ('Y', 'y'):
				break
			elif userCheck in ('N', 'n'):
				check = False
				break
						
def subtraction():
	check = True
	difficulty = 4
	diffCheck = 0
	while(check == True): 
		#Generate the question values at random between 1 & the difficulty level
		A = random.randint(1, difficulty)
		B = random.randint(1, difficulty)
		
		#Ensure the result is positive 
		while(A-B < 0):
			A = random.randint(1, difficulty)
			B = random.randint(1, difficulty)
		
		#Output the question and verify the answer is a valid int
		inputCheck = False
		while(inputCheck == False):
			try:
				print("\nWhat is", A, "-", B, "?")
				inputValue = int(input())
				inputCheck = True
			except ValueError:
				print("The provided input was not a number, please try agian!")
			
		#Verify that the input is the correct answer
		if inputValue == (A - B):
			if difficulty < 10:
				diffCheck += 1
			print("That is correct, well done!")
		else:
			print("\nNot right, the correct answer is:", (A-B))
			if difficulty < 4:
				diffCheck -= 1
				
		#Adjust the difficulty level if required
		if diffCheck <= -3:
			if difficulty > 4:
				difficulty -= 1
			diffCheck = 0
		elif diffCheck >= 3:
			difficulty += 1
			diffCheck = 0
		
		#Check if the user would like to continue - Loop back if yes - exit if no -	
		while(True):
			userCheck = input("Press Y to try another sum or N to stop.\n")
			if userCheck in ('Y', 'y'):
				break
			elif userCheck in ('N', 'n'):
				check = False
				break
				
def multiplication():
	check = True
	difficulty = 4
	diffCheck = 0
	while(check == True):
		#Generate the question values at random between 1 & the difficulty level		
		A = random.randint(1, difficulty)
		B = random.randint(1, difficulty)
		
		#Output the question and verify the answer is a valid int
		inputCheck = False
		while(inputCheck == False):
			try:
				print("\nWhat is", A, "x", B, "?")
				inputValue = int(input())
				inputCheck = True
			except ValueError:
				print("The provided input was not a number, please try agian!")
			
		#Verify that the input is the correct answer
		if inputValue == (A * B):
			if difficulty < 10:
				diffCheck += 1
			print("That is correct, well done!")
		else:
			print("\nNot right, the correct answer is:", (A*B))
			if difficulty < 4:
				diffCheck -= 1

		#Adjust the difficulty level if required
		if diffCheck <= -3:
			if difficulty > 4:
				difficulty -= 1
			diffCheck = 0
		elif diffCheck >= 3:
			difficulty += 1
			diffCheck = 0
			
		#Check if the user would like to continue - Loop back if yes - exit if no -
		while(True):
			userCheck = input("Press Y to try another sum or N to stop.\n")
			if userCheck in ('Y', 'y'):
				break
			elif userCheck in ('N', 'n'):
				check = False
				break
				
def division():
	check = True
	difficulty = 4
	diffCheck = 0
	while(check == True): 
		#Generate the question values at random between 1 & the difficulty level
		A = random.randint(1, difficulty)
		B = random.randint(1, difficulty)
		
		#Ensure the result is positive 
		while(A%B != 0):
			A = random.randint(1, difficulty)
			B = random.randint(1, difficulty)
		
		#Output the question and verify the answer is a valid int
		inputCheck = False
		while(inputCheck == False):
			try:
				print("\nWhat is", A, "/", B, "?")
				inputValue = int(input())
				inputCheck = True
			except ValueError:
				print("The provided input was not a number, please try agian!")
			
		#Verify that the input is the correct answer
		if inputValue == (A/B):
			if difficulty < 10:
				diffCheck += 1
			print("That is correct, well done!")
		else:
			print("\nNot right, the correct answer is:", (A/B))
			if difficulty < 4:
				diffCheck -= 1
				
		#Adjust the difficulty level if required
		if diffCheck <= -3:
			if difficulty > 4:
				difficulty -= 1
			diffCheck = 0
		elif diffCheck >= 3:
			difficulty += 1
			diffCheck = 0
		
		#Check if the user would like to continue - Loop back if yes - exit if no -	
		while(True):
			userCheck = input("Press Y to try another sum or N to stop.\n")
			if userCheck in ('Y', 'y'):
				break
			elif userCheck in ('N', 'n'):
				check = False
				break
				
def mixture():
	check = True
	difficulty = 4
	diffCheck = 0
	map = {1 : "+", 2 : "-", 3 : "x", 4 : "/"}
	while(check == True):
		#Generate the question values at random between 1 & the difficulty level		
		A = random.randint(1, difficulty)
		B = random.randint(1, difficulty)
		C = random.randint(1, 4)
		
		while((C == 2 and A - B < 0) or (C == 4 and A % B > 0)):
			A = random.randint(1, difficulty)
			B = random.randint(1, difficulty)
			
		result = mixResult(A,B,C)
		
		#Output the question and verify the answer is a valid int
		inputCheck = False
		while(inputCheck == False):
			try:
				print("\nWhat is", A, map[C], B, "?")
				inputValue = int(input())
				inputCheck = True
			except ValueError:
				print("The provided input was not a number, please try agian!")
			
		#Verify that the input is the correct answer
		if inputValue == (result):
			if difficulty < 10:
				diffCheck += 1
			print("That is correct, well done!")
		else:
			print("\nNot right, the correct answer is:", result)
			if difficulty < 4:
				diffCheck -= 1

		#Adjust the difficulty level if required
		if diffCheck <= -3:
			if difficulty > 4:
				difficulty -= 1
			diffCheck = 0
		elif diffCheck >= 3:
			difficulty += 1
			diffCheck = 0
			
		#Check if the user would like to continue - Loop back if yes - exit if no -
		while(True):
			userCheck = input("Press Y to try another sum or N to stop.\n")
			if userCheck in ('Y', 'y'):
				break
			elif userCheck in ('N', 'n'):
				check = False
				break
				
def mixResult(A,B,C):
	
	#Calculate the result based on the type of calculation
	if C == 1:
		return A + B
	elif C == 2:
		return A - B
	elif C == 3:
		return A * B
	elif C == 4:
		return A / B