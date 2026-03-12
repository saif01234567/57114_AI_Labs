# # Task 1: CLI Tic-Tac-Toe
# -> We will be taking the example code (the evaluate() function), and expanding it to a playable tic tac toe game, i the terminal (CLI)

# Task 1: CLI Tic-Tac-Toe

def evaluate(b):
    # Check rows
    for row in range(3):
        if b[row][0] == b[row][1] == b[row][2] != '_':
            if b[row][0] == 'x':
                return 10
            else:
                return -10
    # Check columns
    for col in range(3):
        if b[0][col] == b[1][col] == b[2][col] != '_':
            if b[0][col] == 'x':
                return 10
            else:
                return -10
    # Check diagonals
    if b[0][0] == b[1][1] == b[2][2] != '_':
        if b[0][0] == 'x':
            return 10
        else:
            return -10
    if b[0][2] == b[1][1] == b[2][0] != '_':
        if b[0][2] == 'x':
            return 10
        else:
            return -10
    return 0

def print_board(board):
    for row in board:
        print(" | ".join(row))
    print()

def is_moves_left(board):
    for row in board:
        if '_' in row:
            return True
    return False

def play_game():
    board = [['_','_','_'],
             ['_','_','_'],
             ['_','_','_']]
    player = 'x'

    while True:
        print_board(board)
        move = input(f"Player {player}, enter your move (row,col: 0-2,0-2): ")
        try:
            row, col = map(int, move.split(','))
            if board[row][col] == '_':
                board[row][col] = player
            else:
                print("Cell already taken! Try again.")
                continue
        except:
            print("Invalid input! Use format row,col")
            continue

        score = evaluate(board)
        if score == 10:
            print_board(board)
            print("Player X wins!")
            break
        elif score == -10:
            print_board(board)
            print("Player O wins!")
            break
        elif not is_moves_left(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        player = 'o' if player == 'x' else 'x'

if __name__ == "__main__":
    play_game()