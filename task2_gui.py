# Task 2: Tic-Tac-Toe GUI with Tkinter
import tkinter as tk
from tkinter import messagebox

board = [['_','_','_'],
         ['_','_','_'],
         ['_','_','_']]
player = 'x'

def evaluate(b):
    for row in range(3):
        if b[row][0] == b[row][1] == b[row][2] != '_':
            return 10 if b[row][0]=='x' else -10
    for col in range(3):
        if b[0][col] == b[1][col] == b[2][col] != '_':
            return 10 if b[0][col]=='x' else -10
    if b[0][0] == b[1][1] == b[2][2] != '_':
        return 10 if b[0][0]=='x' else -10
    if b[0][2] == b[1][1] == b[2][0] != '_':
        return 10 if b[0][2]=='x' else -10
    return 0

def on_click(r, c):
    global player
    if board[r][c] == '_':
        board[r][c] = player
        buttons[r][c]['text'] = player.upper()
        score = evaluate(board)
        if score == 10:
            messagebox.showinfo("Game Over", "Player X wins!")
            root.quit()
        elif score == -10:
            messagebox.showinfo("Game Over", "Player O wins!")
            root.quit()
        elif all(cell != '_' for row in board for cell in row):
            messagebox.showinfo("Game Over", "It's a draw!")
            root.quit()
        player = 'o' if player == 'x' else 'x'

root = tk.Tk()
root.title("Tic-Tac-Toe")
buttons = [[tk.Button(root, text=' ', width=10, height=5, command=lambda r=i, c=j: on_click(r,c))
            for j in range(3)] for i in range(3)]

for i in range(3):
    for j in range(3):
        buttons[i][j].grid(row=i, column=j)

root.mainloop()