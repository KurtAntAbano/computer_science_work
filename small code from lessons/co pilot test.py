# Connect Four game

# Constants
BOARD_WIDTH = 7
BOARD_HEIGHT = 6

# Global variables
board = []
current_player = 'X'

def create_board():
  """Create a new, empty board"""
  for i in range(BOARD_HEIGHT):
    board.append([' '] * BOARD_WIDTH)

def display_board():
  """Display the current state of the board"""
  print(' 1  2  3  4  5  6  7 ')
  for row in board:
    print('|'.join(row))

def get_move(player):
  """Get the player's move"""
  while True:
    move = input(f'{player}, enter your move (1-7): ')
    try:
      move = int(move) - 1
      if move >= 0 and move < BOARD_WIDTH and board[0][move] == ' ':
        return move
      else:
        print('Invalid move! Try again.')
    except ValueError:
      print('Invalid input! Enter a number from 1 to 7.')

def make_move(player, move):
  """Make a move on the board"""
  for i in range(BOARD_HEIGHT-1, -1, -1):
    if board[i][move] == ' ':
      board[i][move] = player
      return

def has_won(player):
  """Check if the player has won"""
  # check for horizontal wins
  for row in board:
    for i in range(BOARD_WIDTH-3):
      if row[i] == player and row[i+1] == player and row[i+2] == player and row[i+3] == player:
        return True
  # check for vertical wins
  for col in range(BOARD_WIDTH):
    for i in range(BOARD_HEIGHT-3):
      if board[i][col] == player and board[i+1][col] == player and board[i+2][col] == player and board[i+3][col] == player:
        return True
  # check for diagonal wins
  for col in range(BOARD_WIDTH-3):
    for i in range(BOARD_HEIGHT-3):
      if board[i][col] == player and board[i+1][col+1] == player and board[i+2][col+2] == player and board[i+3][col+3] == player:
        return True
      if board[i][col+3] == player and board[i+1][col+2] == player and board[i+2][col+1] == player and board[i+3][col] == player:
        return True
  return False

def main():
  """Main game loop"""
  create_board()
  while True:
    display_board()

