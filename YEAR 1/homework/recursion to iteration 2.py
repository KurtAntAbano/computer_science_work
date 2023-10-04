def generateObstacle(dicenumber):
    while dicenumber != 0:
        x = randomNumber(0, 7)
        y = randomNumber(0, 7)
        board(x, y) = new obstacle()
        dicenumber -= 1
    return True




