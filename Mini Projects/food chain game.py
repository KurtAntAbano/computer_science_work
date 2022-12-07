#Food Chain Game Using Python - www.101computing.net/food-chain-game-using-python/
import random

foodChain = ["Grass" , "Grasshopper" , "Frog", "Snake", "Eagle"]

foodChainLength = len(foodChain)

player1Position = random.randint(0,foodChainLength-1)
player1Organism = foodChain[player1Position]

print("Player 1 Organism: " + player1Organism)

#Complete code here to select a different organism for the computer

#Then work out who has the highest position to identify the winner (Player or computer)
#2nd player

player2Position = random.randint(0,foodChainLength-1)
while player2Position == player1Position:
    player2Position = random.randint(0, foodChainLength - 1)
player2Organism = foodChain[player2Position]

print("Player 2  Organism: " + player2Organism)

if player1Position > player2Position:
    print("Player 1 wins")
else:
    print("Player 2 wins")