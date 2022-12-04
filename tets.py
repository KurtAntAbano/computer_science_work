# var = input("Hello")
# match var:
#     case "Hello":
#         print("Yes")

# def fun1(column):
#
#     match column:
#         case "A":
#             print("hi")
# def fun():
#     column = input("please enter column")
#     fun1(column)
#
# fun()

board = [["a","a","a","B","a"],
         ["a","a","B","a","a"],
         ["a","B","a","a","a"],
         ["B","a","a","a","a"]]

colour = "B"
for i in range(0, len(board)):
    print(board[i])

for i in range(0, len(board)):
    for l in range(0, 5):
        if board[i][l] == colour and board[i + 1][l + 1] == colour and board[i + 2][l + 2] == colour and \
                board[i + 3][l + 3] == colour:
            print("true")

# board = [["O", "O", "O", "O", "O", "O", "O"],
#          ["O", "O", "O", "O", "O", "O", "O"],
#          ["O", "O", "O", "O", "O", "O", "O"],
#          ["R", "O", "O", "O", "O", "O", "O"],
#          ["R", "O", "O", "O", "O", "O", "O"],
#          ["R", "O", "O", "O", "O", "O", "O"],
#          ["R", "O", "O", "0", "O", "O", "O"],
#          ["A", "B", "C", "D", "E", "F", "G"]]
#
# stack_pointers = [6, 6, 6, 6, 6, 6, 6]
#
#
# def is_winner(colour):
#     temp = 0
#     for i in range(0, len(board)):
#         for l in range(0, len(board) - 1):
#             if board[i][l] == colour and board[i][l + 1] == colour and board[i][l + 2] == colour and board[i][
#                 l + 3] == colour:
#                 return True
#
#     for i in range(0, len(board)):
#         for l in range(0, len(board) - 1):
#             if board[i][l] == colour and board[i + 1][l] == colour and board[i + 2][l] == colour and board[i + 3][
#                 l] == colour:
#                 return True
#
#
# colour = "R"
# print(is_winner(colour))
