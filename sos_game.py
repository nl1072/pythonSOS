import random
from tkinter import *

class SOSGame:
    """Class representing a game of SOS"""
    def __init__(self, board_size, game_mode, vs_computer):
        if board_size <= 2:
            raise RuntimeError('board_size must be greater than or equal to 3')
        self.board_size = board_size
        self.gamemode = game_mode
        self.vs_computer = vs_computer

        self.board = [[' ' for x in range(self.board_size)] for y in range(self.board_size)]
        self.players = ['P1','P2']
        self.current_player = random.choice(self.players)
        self.pieces = ['S', 'O']
        self.current_piece_p1 = self.pieces[0]
        self.current_piece_p2 = self.pieces[0]

    def get_board_size(self):
        return self.board_size
    def get_gamemode(self):
        return self.gamemode
    def get_vs_computer(self):
        return self.vs.computer
    def get_board(self):
        return self.board
    def get_current_player(self):
        return self.current_player
    def get_player_piece(self, player):
        if player == 'P1':
            return self.current_piece_p1
        if player == 'P2':
            return self.current_piece_p2
    def get_current_player_piece(self):
        if self.current_player == 'P1':
            return self.current_piece_p1
        if self.current_player == 'P2':
            return self.current_piece_p2
    def get_cell(self, row, column):
        return self.board[row][column]

    def make_move(self, row, column):
        """Makes a move for the current player at the specified cell, then swaps turn to the next player.
        
            Args:
            row: a valid row position.
            column: a valid column position
        
        """
        if self.board[row][column] == ' ':
            if self.current_player == self.players[0]:
                self.board[row][column] = self.current_piece_p1
                if self.current_piece_p1 == self.pieces[0]:
                    self.current_piece_p1 = self.pieces[1]
                else:
                    self.current_piece_p1 = self.pieces[0]
                self.current_player = self.players[1]
            else:
                self.board[row][column] = self.current_piece_p2
                if self.current_piece_p2 == self.pieces[0]:
                    self.current_piece_p2 = self.pieces[1]
                else:
                    self.current_piece_p2 = self.pieces[0]
                self.current_player = self.players[0]
            

    def check_winner(self):
        """Checks if a player has won"""

    def new_game(self):
        """Starts a new game"""
        self.__init__(self.board_size, self.gamemode, self.vs_computer)

    def print_board(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                print(self.board[row][col],end='')
                if col == self.board_size - 1:
                    break
                else:
                    print(' | ',end='')
            if row == self.board_size - 1:
                break
            else:
                print('\n----------')
