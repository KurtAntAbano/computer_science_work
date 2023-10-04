board = [["O ", "X ", "X ", "X "],
         ["X ", "X ", "X ", "X "],
         ["X ", "X ", "X ", "X "],
         ["X ", "X ", "X ", "X "],
         ["X ", "X ", "X ", "X "],
         ["X ", "X ", "X ", "X "]]

character_row = 0
character_column = 0


def show_board():
    global board
    for i in range(0, len(board)):
        print(' '.join(board[i]))


def move(row, column):
    global board, character_row, character_column
    board[character_row][character_column] = "X "
    board[row][column] = "O "

    character_row = row
    character_column = column


def main():
    row_value = int(input("enter row value!"))
    column_value = int(input("enter column value!"))
    show_board()
    move(row_value, column_value)
    print("\n")
    show_board()


main()


