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
#
# board = [["a","a","a","B","a"],
#          ["a","a","B","a","a"],
#          ["a","B","a","a","a"],
#          ["B","a","a","a","a"]]
#
# colour = "B"
# for i in range(0, len(board)):
#     print(board[i])
#
# for i in range(0, len(board)):
#     for l in range(0, 5):
#         if board[i][l] == colour and board[i + 1][l + 1] == colour and board[i + 2][l + 2] == colour and \
#                 board[i + 3][l + 3] == colour:
#             print("true")

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

# print("\e[0;31m Hello world")
# print("\033[1;31m This text is Bright Green \033[m \nyo")
# colour1 = ("\033[1;31m R \033[m")
# print(colour1)
# colour1 = "\033[1;33m Y \033[m"
# colour1 = "\033[1;31m R \033[m"


#chatgpt
# import tkinter as tk
# def hello():
#     print("hello")
#
# window = tk.Tk()
#
# button = tk.Button(window, text = "hello",command = hello)
# button.pack()
# button2 = tk.Button(window, text = "hello",command = hello)
# button2.pack()
# button3 = tk.Button(window, text = "hello",command = hello)
# button3.pack()
#
# window.mainloop()
colourDict = {"Black": 0, "Brown": 1, "Red": 2, "Orange": 3, "Yellow": 4,
              "Green": 5, "Blue": 6, "Violet": 7, "Grey": 8, "White": 9,
              "Gold": 0, "Silver": 0, "No Band": 0}

# colours = list(colourDict)
#
# window = tk.Tk()
# for i in range(13):
#     button[i] = tk.Button(window, text=colours[i], command=colour_append)
#     button[i].pack()
# window.mainloop()

window = tk.Tk()
b1 = tk.Button(window,text = "Black")

