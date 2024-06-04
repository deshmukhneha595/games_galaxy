import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        for i in range(9):
            button = tk.Button(self.root, text=' ', font=('normal', 40), width=5, height=2,
                               command=lambda i=i: self.on_button_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

    def on_button_click(self, index):
        if self.board[index] == ' ' and self.current_player == 'X':
            self.make_move(index)
            if not self.check_game_over():
                self.current_player = 'O'
                self.root.after(500, self.automated_move)

    def automated_move(self):
        available_moves = [i for i, cell in enumerate(self.board) if cell == ' ']
        if available_moves:
            index = random.choice(available_moves)
            self.make_move(index)
            self.check_game_over()
            self.current_player = 'X'

    def make_move(self, index):
        self.board[index] = self.current_player
        self.buttons[index].config(text=self.current_player)

    def check_game_over(self):
        if self.check_winner(self.current_player):
            messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
            self.reset_game()
            return True
        elif self.check_draw():
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            self.reset_game()
            return True
        return False

    def check_winner(self, player):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
                          (0, 4, 8), (2, 4, 6)]             # diagonals
        return any(all(self.board[pos] == player for pos in condition) for condition in win_conditions)

    def check_draw(self):
        return all(cell != ' ' for cell in self.board)

    def reset_game(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        for button in self.buttons:
            button.config(text=' ')

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
