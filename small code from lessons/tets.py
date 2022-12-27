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

import tkinter as tk
import random

# The Monty Hall problem game

def play_game():
    # Randomly select the winning door
    winning_door = random.randint(1, 3)

    # Randomly select the door chosen by the player
    chosen_door = random.randint(1, 3)

    # Monty Hall opens a door that is not the winning door and not the chosen door
    opened_door = random.choice([door for door in range(1, 4) if door != winning_door and door != chosen_door])

    # Calculate the door that remains closed
    closed_door = [door for door in range(1, 4) if door != opened_door and door != chosen_door][0]

    # Calculate the probability of winning if the player sticks with their original choice
    probability_staying = 1 if chosen_door == winning_door else 0

    # Calculate the probability of winning if the player switches to the closed door
    probability_switching = 1 if closed_door == winning_door else 0

    # Display the results
    result_text.set(f"Winning door: {winning_door}\n"
                    f"Chosen door: {chosen_door}\n"
                    f"Opened door: {opened_door}\n"
                    f"Closed door: {closed_door}\n"
                    f"Probability of winning if staying: {probability_staying}\n"
                    f"Probability of winning if switching: {probability_switching}")

# Create the main window
window = tk.Tk()
window.title("Monty Hall Problem")

# Add a button widget to start the game
play_button = tk.Button(text="Play", command=play_game)
play_button.pack()

# Add a text widget to display the results
result_text = tk.StringVar()
result_label = tk.Label(textvariable=result_text)
result_label.pack()

# Start the GUI event loop
window.mainloop()
