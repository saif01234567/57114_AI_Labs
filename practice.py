# IMPLEMENTING A SAMPLE BOARD!!!

def evaluate(b):
    # Checking rows for X or O victory
    for row in range(3):
        if b[row][0] == b[row][1] == b[row][2]:
            if b[row][0] == 'x':
                return 10
            elif b[row][0] == 'o':
                return -10

    # Checking columns for X or O victory
    for col in range(3):
        if b[0][col] == b[1][col] == b[2][col]:
            if b[0][col] == 'x':
                return 10
            elif b[0][col] == 'o':
                return -10

    # Checking diagonals for X or O victory
    if b[0][0] == b[1][1] == b[2][2]:
        if b[0][0] == 'x':
            return 10
        elif b[0][0] == 'o':
            return -10

    if b[0][2] == b[1][1] == b[2][0]:
        if b[0][2] == 'x':
            return 10
        elif b[0][2] == 'o':
            return -10

    # If none have won, return 0
    return 0

# Driver code
if __name__ == "__main__":
    board = [['x','_','o'],
             ['x','o','o'],
             ['x','_','_']]

    value = evaluate(board)
    print("The value of this board is", value)