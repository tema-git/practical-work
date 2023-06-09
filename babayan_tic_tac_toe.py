# -*- coding: utf-8 -*-
"""Babayan_tic-tac-toe.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZXWH7rYemGfeoA9NIUwAccPFF5Y4-ACN
"""





def print_board(board):
    print("-------------")
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print("-------------")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print("-------------")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |")
    print("-------------")

def check_win(board, player):
    if (board[0] == player and board[1] == player and board[2] == player) or \
       (board[3] == player and board[4] == player and board[5] == player) or \
       (board[6] == player and board[7] == player and board[8] == player) or \
       (board[0] == player and board[3] == player and board[6] == player) or \
       (board[1] == player and board[4] == player and board[7] == player) or \
       (board[2] == player and board[5] == player and board[8] == player) or \
       (board[0] == player and board[4] == player and board[8] == player) or \
       (board[2] == player and board[4] == player and board[6] == player):
        return True
    else:
        return False

def tic_tac_toe():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    player = "X"
    game_over = False
    print("Добро пожаловать в крестики-нолики!")
    print_board(board)
    while not game_over:
        print("Сейчас ход " + player)
        move = input("Введите позицию (1-9): ")
        if move == 'конец игры':
            game_over = True
        else:
            move = int(move)-1
            if board[move] == " ":
                board[move] = player
                print_board(board)
                if check_win(board, player):
                    print(player + " победил!")
                    game_over = True
                elif " " not in board:
                    print("Ничья!")
                    game_over = True
                else:
                    player = "O" if player == "X" else "X"
            else:
                print("Тут занято. Введите другое значение.")

tic_tac_toe()











