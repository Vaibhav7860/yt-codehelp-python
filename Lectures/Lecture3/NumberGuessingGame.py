import random

r = random.randint(1,20)
print("Enter a number to guess : ")
while(True):
	userInput = int(input())
	if(userInput < r):
		print("Wrong guess, try a greater number")
	elif(userInput > r):
		print("Wrong guess, try a smaller number")
	else:
		print("Correct guess!")
		break