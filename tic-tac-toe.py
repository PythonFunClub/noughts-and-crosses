
import random
import sys
roundCount = 0
randomSquares =[]
board = [" "," "," "," "," "," "," "," "," "]
score = {
	" ": 0,
	"X": -1,
	"O": 1
}

def printGuidance():
# print the square number for guidance
	print("-------------------")
	print("| ",1," | ",2," | ",3," | ")
	print("-------------------")
	print("| ",4," | ",5," | ",6," | ")
	print("-------------------")
	print("| ",7," | ",8," | ",9," | ")
	print("-------------------")

# after each round print the board
def printBoard():

	print("-------------------")
	print("| ",board[0]," | ",board[1]," | ",board[2]," | ")
	print("-------------------")
	print("| ",board[3]," | ",board[4]," | ",board[5]," | ")	
	print("-------------------")
	print("| ",board[6]," | ",board[7]," | ",board[8]," | ")	
	print("-------------------")


def humanTurn():
	# ask for a square number
	while True:
		try:
			i = int(input("Select a square (1-9) or 0 to quit ")) - 1
			if i == -1:
				sys.exit()

			# check the square is empty if not put an O in it
			if board[i] == " ":
				board[i] = "O"
				# end of human go so break
				break
			else:
				# if the square is not empty prompt for another squaure
				print("That square has been taken, please try another")
				continue
		except Exception as e:
			print("Please enter a valid integer")

def compTurn():
	while True :
		ran = random.randint(0,8)
		if board[ran] == " ":
			board[ran] = "X"
			break

def checkWinner():
	# check each row 
	totalRowScore = 0
	for i in range(0,3):
		a = i * 3
		b = a + 3
		totalRowScore = 0
		for x in range(a,b): 
			totalRowScore += score.get(board[x], 0)
		if totalRowScore == 3 or totalRowScore == -3:
			break
	
	# check each column 
	totalColScore = 0
	for i in range(-1,2):
		a = i + 1
		b = a + 7
		totalColScore = 0
		for x in range(a,b,3): 
			totalColScore += score.get(board[x], 0)
		if totalColScore == 3 or totalColScore == -3:
			break

	# check top left to bottom right 
	totalDiagonalScoreTL = 0
	for j in range(0,9,4):
		totalDiagonalScoreTL += score.get(board[j], 0)
	# check top right to bottom left 
	totalDiagonalScoreTR = 0
	for j in range(2,8,2):
		totalDiagonalScoreTR += score.get(board[j], 0)

	if totalRowScore == -3 or totalDiagonalScoreTL == -3 or totalDiagonalScoreTR == -3 or totalColScore == -3:
		return "me - the computer"
	if totalRowScore == 3 or totalDiagonalScoreTL == 3 or totalDiagonalScoreTR == 3 or totalColScore == 3:
		printBoard()
		return "you - congratulations"


def turns(firstGo):
	if firstGo == "human":
		humanTurn()

	while checkWinner() is None:

		if " " in board:
			compTurn()
			printBoard()
			if checkWinner() is not None:
				print('The winner is ', checkWinner())
				break

			humanTurn()
			if checkWinner() is not None:
				print('The winner is ', checkWinner())	
				break		
		else:
			printBoard()
# check to see if the last go wins the game
			if checkWinner() is not None:
				print("The winner is ", checkWinner())
				break
			print("It's a draw")
			break

def coinToss():
	while True:
		headsOrTails = input("Heads or tails (h or t) ")

		if headsOrTails == "h":
			coinCall = "heads"
			break
		elif headsOrTails == "t":
			coinCall = "tails"
			break
		else:
			print("Invalid input")

	ran = random.randint(0,1)
	if ran == 0:
		coinFace = "heads"
	elif ran == 1:
		coinFace = "tails" 
	else:
		print("something went wrong")

	print("It's " , coinFace)


	if coinCall == coinFace:
		firstGo = "human"
		print ("You won the Toss, you go first")

	else:
		firstGo = "computer"
		print ("You lost the Toss, I'm going first")

	printGuidance()

	return firstGo


coinT = coinToss ()
turns(coinT)