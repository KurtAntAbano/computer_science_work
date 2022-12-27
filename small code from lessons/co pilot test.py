# # Connect Four game
#
# # Constants
# BOARD_WIDTH = 7
# BOARD_HEIGHT = 6
#
# # Global variables
# board = []
# current_player = 'X'
#
# def create_board():
#   """Create a new, empty board"""
#   for i in range(BOARD_HEIGHT):
#     board.append([' '] * BOARD_WIDTH)
#
# def display_board():
#   """Display the current state of the board"""
#   print(' 1  2  3  4  5  6  7 ')
#   for row in board:
#     print('|'.join(row))
#
# def get_move(player):
#   """Get the player's move"""
#   while True:
#     move = input(f'{player}, enter your move (1-7): ')
#     try:
#       move = int(move) - 1
#       if move >= 0 and move < BOARD_WIDTH and board[0][move] == ' ':
#         return move
#       else:
#         print('Invalid move! Try again.')
#     except ValueError:
#       print('Invalid input! Enter a number from 1 to 7.')
#
# def make_move(player, move):
#   """Make a move on the board"""
#   for i in range(BOARD_HEIGHT-1, -1, -1):
#     if board[i][move] == ' ':
#       board[i][move] = player
#       return
#
# def has_won(player):
#   """Check if the player has won"""
#   # check for horizontal wins
#   for row in board:
#     for i in range(BOARD_WIDTH-3):
#       if row[i] == player and row[i+1] == player and row[i+2] == player and row[i+3] == player:
#         return True
#   # check for vertical wins
#   for col in range(BOARD_WIDTH):
#     for i in range(BOARD_HEIGHT-3):
#       if board[i][col] == player and board[i+1][col] == player and board[i+2][col] == player and board[i+3][col] == player:
#         return True
#   # check for diagonal wins
#   for col in range(BOARD_WIDTH-3):
#     for i in range(BOARD_HEIGHT-3):
#       if board[i][col] == player and board[i+1][col+1] == player and board[i+2][col+2] == player and board[i+3][col+3] == player:
#         return True
#       if board[i][col+3] == player and board[i+1][col+2] == player and board[i+2][col+1] == player and board[i+3][col] == player:
#         return True
#   return False
#
# def main():
#   """Main game loop"""
#   create_board()
#   while True:
#     display_board()
#
#---------------------------------------------------------------------------------
# import tkinter as tk
#
# # Create a chessboard as a 2D list of buttons
# chessboard = []
# for i in range(8):
#     row = []
#     for j in range(8):
#         button = tk.Button(text=" ", font=("Arial", 32), width=2, height=1)
#         button.grid(row=i, column=j)
#         row.append(button)
#     chessboard.append(row)
#
# # Create a label to display the current player's turn
# turn_label = tk.Label(text="White's turn", font=("Arial", 16))
# turn_label.grid(row=8, column=0, columnspan=8)
#
# # Create a function to handle button clicks
# def button_clicked(i, j):
#     # Get the text on the button that was clicked
#     text = chessboard[i][j]["text"]
#     # If the button is empty, place a piece on it
#     if text == " ":
#         # Set the text on the button to the current player's color
#         if turn_label["text"] == "White's turn":
#             chessboard[i][j]["text"] = "W"
#             # Switch to black's turn
#             turn_label["text"] = "Black's turn"
#         else:
#             chessboard[i][j]["text"] = "B"
#             # Switch to white's turn
#             turn_label["text"] = "White's turn"
#
# # Bind the button_clicked function to each button on the chessboard
# for i in range(8):
#     for j in range(8):
#         chessboard[i][j]["command"] = lambda i=i, j=j: button_clicked(i, j)
#
# # Run the Tkinter event loop
# tk.mainloop()
#------------------------------------------------------------
import tkinter as tk

class Connect4:
    def init(self):
        self.root = tk.Tk()
        self.root.title("Connect 4")
        self.canvas = tk.Canvas(self.root, width=400, height=600)
        self.canvas.pack()

        # Create a 2D list to represent the game board
        self.board = [[0] * 7 for _ in range(6)]

        # Draw the game board
        for row in range(6):
            for col in range(7):
                x1, y1 = col * 50, row * 50
                x2, y2 = x1 + 50, y1 + 50
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")

        # Bind the left mouse button click event to the canvas
        self.canvas.bind("<Button-1>", self.play)

        # Start the main loop
        self.root.mainloop()

    def play(self, event):
        # Calculate the column where the player clicked
        col = event.x // 50

        # Find the first empty row in the column
        for row in range(5, -1, -1):
            if self.board[row][col] == 0:
                self.board[row][col] = 1
                x1, y1 = col * 50, row * 50
                x2, y2 = x1 + 50, y1 + 50
                self.canvas.create_oval(x1 + 10, y1 + 10, x2 - 10, y2 - 10, fill="red")
                break

# if name == "main":
#     game = Connect4()
input()