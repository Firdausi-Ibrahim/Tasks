import random
import time


# Function to print the Tic-Tac-Toe board
def print_board(board):
    print(f"""    tic tac toe
    -----------
     {board[0]} | {board[1]} | {board[2]}
    -----------
     {board[3]} | {board[4]} | {board[5]}
    -----------
     {board[6]} | {board[7]} | {board[8]}
    """)


# Function to check for a win
def check_win(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False


# Function to check for a draw
def check_draw(board):
    return all(cell in ['X', 'O'] for cell in board)


# Function to get user's move
def get_user_move(board, user_name):
    while True:
        try:
            move = int(input(f"{user_name}, it's your turn to play (1-9): \033[1;34m player(X)\033[0;0m: ")) - 1 # we used ansi escape codes to change the text to blue
            if board[move] not in ['X', 'O']:
                return move
            else:
                print("This spot is already taken.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")


# Function to get computer's move
def get_computer_move(board):
    empty_cells = [i for i, cell in enumerate(board) if cell not in ['X', 'O']]
    return random.choice(empty_cells)


# Function to add delay with loading message
def loading_message():
    print("Loading... ")
    for _ in range(2):
        time.sleep(1)
    print()


# Main game function
def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe! Let's have some fun!")
    user_name = input("Enter your name: ")
    print(f"Hello, {user_name}! You will be playing as 'X' and the computer will be 'O'.")
    print("Enter the number corresponding to the position you want to mark.")

    board = [str(i + 1) for i in range(9)]
    print_board(board)  # Print the board with numbers 1-9

    while True:
        # User's move
        user_move = get_user_move(board, user_name)
        board[user_move] = 'X'
        print_board(board)
        if check_win(board, 'X'):
            loading_message()
            print(f"Nice one, {user_name}! You win! 🎉")
            break
        if check_draw(board):
            loading_message()
            print(f"It's a draw, {user_name}! 🤝")
            break

        # Computer's move
        print(random.choice(["Thinking...", "Hmm, let me see...", "My turn!"]))
        loading_message()
        computer_move = get_computer_move(board)
        board[computer_move] = 'O'
        print_board(board)
        if check_win(board, 'O'):
            loading_message()
            print("Oh no! The computer wins! 🤖")
            break
        if check_draw(board):
            loading_message()
            print(f"It's a draw, {user_name}! 🤝")
            break


# Start the game
if __name__ == "__main__":
    tic_tac_toe()
