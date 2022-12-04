board = [["O", "O", "O", "O", "O", "O", "O"],
         ["O", "O", "O", "O", "O", "O", "O"],
         ["O", "O", "O", "O", "O", "O", "O"],
         ["O", "O", "O", "O", "O", "O", "O"],
         ["O", "O", "O", "O", "O", "O", "O"],
         ["O", "O", "O", "O", "O", "O", "O"],
         ["O", "O", "O", "O", "O", "O", "O"],
         ["A", "B", "C", "D", "E", "F", "G"]]

stack_pointers = [6, 6, 6, 6, 6, 6, 6]

p1_name = ""
colour1 = ""
p2_name = ""
colour2 = ""
#global statements

def show_board():
    global board
    for i in range(0, len(board)):
        print(board[i])
    #show board through printing each array through for loops


def data_entry():
    global p1_name, colour1, p2_name, colour2
    p1_name = input("Player 1, input your name")
    colour1 = input("Choose colour, R or Y")
    p2_name = input("\nPlayer 2, input you name")
    if colour1 == "R":
        colour2 = "Y"
    elif colour1 == "Y":
        colour2 = "R"
    print(p2_name + ", you will be", colour2, "then\n")


    # find the row value
    # convert "A" into number
    # find column value
    # board[row][col] = l
def update_board(x, colour):
    if x == "A":
        board[stack_pointers[0]][0] = colour
        stack_pointers[0] -= 1

    elif x == "B":
        board[stack_pointers[1]][1] = colour
        stack_pointers[1] -= 1

    elif x == "C":
        board[stack_pointers[2]][2] = colour
        stack_pointers[2] -= 1

    elif x == "D":
        board[stack_pointers[3]][3] = colour
        stack_pointers[3] -= 1

    elif x == "E":
        board[stack_pointers[4]][4] = colour
        stack_pointers[4] -= 1

    elif x == "F":
        board[stack_pointers[5]][5] = colour
        stack_pointers[5] -= 1

    elif x == "G":
        board[stack_pointers[6]][6] = colour
        stack_pointers[6] -= 1

def is_winner(colour):
    for i in range(0,len(board)):
        for l in range(0,len(board)-1):
            if board[i][l] == colour and board[i][l + 1] == colour and board[i][l + 2] == colour and board[i][l + 3] == colour:
                return True

    for i in range(0,len(board)):
        for l in range(0,len(board)-1):
            if board[i][l] == colour and board[i + 1][l] == colour and board[i + 2][l] == colour and board[i + 3][l] == colour:
                return True

def play():
    attempt = 0
    winner = False

    while not winner:
        if attempt % 2 == 0:
            column = input(p1_name + " please enter a column")
            update_board(column, colour1)
            show_board()
            winner = is_winner(colour1)


        else:
            column = input(p2_name +" please enter a column")
            update_board(column, colour2)
            show_board()
            winner = is_winner(colour2)

        attempt += 1


    if attempt % 2 == 0:
        print(p2_name, "WINS!!!!")

    else:
        print(p1_name, "WINS!!!!")


def main():
    show_board()
    data_entry()
    play()

main()