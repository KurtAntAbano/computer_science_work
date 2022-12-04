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

board = [["a","a","a","a","a"],
        ["a","a","a","a","a"],
        ["a","a","a","a","a"],
        ["B","B","B","B","a"]]

for i in range(0, len(board)):
    print(board[i])

for i in range(0,len(board)):
    for l in range(0,len(board)):
        if board[i][l] == "B" and board[i][l + 1] == "B" and board[i][l + 2] == "B" and board[i][l + 3] == "B":
            print("U win")
