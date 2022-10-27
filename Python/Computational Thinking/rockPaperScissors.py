#Get Inputs
print("Please enter 'rock', 'paper', or 'scissors' for each player.")
player1 = input("Player 1: ")
player2 = input("Player 2: ")

#Determine Outcome
#Test if a tie
if player1 == player2:
    answer = "It's a tie!"
#Test if player 1 wins
if (player1 == "rock" and player2 == "scissors") or (player1 == "paper" and player2 == "rock") or (player1 == "scissors" and player2 == "paper"):
    answer = "Player 1 wins!"
#Test if player 2 wins
if (player2 == "rock" and player1 == "scissors") or (player2 == "paper" and player1 == "rock") or (player2 == "scissors" and player1 == "paper"):
    answer = "Player 2 wins!"
    
#Output Answer
print(answer)