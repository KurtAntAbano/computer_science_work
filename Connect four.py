board = [[0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         ["A","B","C","D","E","F","G"]]

stack_pointers =[5,5,5,5,5,5,5]

p1_name = ""
colour1 = ""
p2_name = ""
colour2 = ""

def show_board():
    global board
    for i in range(0,len(board)):
        print(board[i])

def data_entry():
    global p1_name, colour1, p2_name, colour2
    p1_name = input("input your name")
    colour1 = input("Choose colour, R or Y")
    p2_name = input("input you name")
    colour2 = input("Choose colour")








def update_board(l):
    # find the row value

    #convert "A" into number
    # find column value


    #board[row][col] = l
    show_board()


def play():
    attempt = 0
    if attempt % 2 == 0:
        column = input("please enter column")




def main():
    show_board()
    data_entry()
    print(p1_name, colour1, p2_name, colour2)

main()