import os

# Initialize the board
board = {i: [None] * 6 for i in range(7)}
turn_count = 0
MAX_COUNT = 42

# Input player names
player_1_name = input("What is player one's name: ")
player_2_name = input("What is player two's name: ")

def print_board():
    def display(val):
        return val if val is not None else '.'
    
    for row in range(5, -1, -1):
        print("| " + " | ".join(display(board[col][row]) for col in range(7)) + " |")
    print("-" * 29)

class User:
    def __init__(self, name, shape):
        self.name = name
        self.shape = shape
    
    def __repr__(self):
        return f"{self.name} uses shape: {self.shape}"
    
    def add_piece(self, col):
        global turn_count
        if col not in board:
            print("Invalid column. Try again!")
            return False
        
        for i in range(6):
            if board[col][i] is None:
                board[col][i] = self.shape
                turn_count += 1
                return True
        
        print("Column is full. Try another column.")
        return False

def check_win(shape):
    for row in range(6):
        for col in range(4):
            if all(board[c][row] == shape for c in range(col, col + 4)):
                return True
    
    for col in range(7):
        for row in range(3):
            if all(board[col][r] == shape for r in range(row, row + 4)):
                return True
    
    for col in range(4):
        for row in range(3):
            if all(board[col + i][row + i] == shape for i in range(4)):
                return True
    
    for col in range(4):
        for row in range(3, 6):
            if all(board[col + i][row - i] == shape for i in range(4)):
                return True

    return False

def user_move(player):
    while True:
        try:
            col = int(input(f"{player.name}, choose a column (0-6) to drop your '{player.shape}': "))
            if 0 <= col <= 6:
                if player.add_piece(col):
                    return
            else:
                print("Column must be between 0 and 6.")
        except ValueError:
            print("Please enter a valid integer.")

# Initialize players
player_1 = User(player_1_name, "X")
player_2 = User(player_2_name, "O")

# Game loop
current_player = player_1

while turn_count < MAX_COUNT:
    print_board()
    user_move(current_player)

    if check_win(current_player.shape):
        print_board()
        print(f"🎉 {current_player.name} wins! 🎉")
        break
    
    current_player = player_2 if current_player == player_1 else player_1

else:
    print_board()
    print("It's a tie! No more moves left.")