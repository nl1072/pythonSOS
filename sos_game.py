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
        self.p1_score = 0
        self.p2_score = 0

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
    
    def set_board_size(self, new_board_size):
        self.board_size = new_board_size
    def set_gamemode(self, new_gamemode):
        self.gamemode = new_gamemode
    def set_vs_computer(self, new_vs_computer):
        self.vs_computer = new_vs_computer

    def check_trios(self, last_played_letter, last_played_row, last_played_column, trio_token='SOS',):
        """Checks if there are valid trios.
        
        Args:
            gamemode: a valid gamemode.
            last_played_letter: the last letter placed on the board.
            last_played_row: the row position of the last move.
            last_played_column: the column position of the last move.
            trio_token: a valid win token. default 'SOS'
        """
        num_trios = 0
        if last_played_letter ==  'S':
            # check all lines stemming from this cell
            for row in range(self.board_size):
                    for column in range(self.board_size):
                        found_trio =False
                        try:
                            # sw
                            if (f'{self.board[last_played_row][last_played_column]}{self.board[last_played_row+1][last_played_column-1]}{self.board[last_played_row+2][last_played_column-2]}') == trio_token:
                                num_trios += 1
                                found_trio = True
                                break
                        except IndexError:
                            pass
                        try:
                           # w
                            if (f'{self.board[last_played_row][last_played_column]}{self.board[last_played_row][last_played_column-1]}{self.board[last_played_row][last_played_column-2]}') == trio_token:
                                num_trios += 1
                                found_trio = True
                                break
                        except IndexError:
                            pass
                        try:
                            # nw
                            if (self.board[last_played_row][last_played_column] + self.board[last_played_row-1][last_played_column-1] + self.board[last_played_row-2][last_played_column-2]) == trio_token:
                                num_trios += 1
                                found_trio = True
                                break
                        except IndexError:
                            pass
                        try:
                            # n
                            if (self.board[last_played_row][last_played_column] + self.board[last_played_row-1][last_played_column] + self.board[last_played_row-2][last_played_column]) == trio_token:
                                num_trios += 1
                                found_trio = True
                                break
                        except IndexError:
                            pass
                        try:
                            # ne
                            if (self.board[last_played_row][last_played_column] + self.board[last_played_row-1][last_played_column+1] + self.board[last_played_row-2][last_played_column+2]) == trio_token:
                                num_trios += 1
                                found_trio = True
                                break
                        except IndexError:
                            pass
                        try:
                            # e
                            if (self.board[last_played_row][last_played_column] + self.board[last_played_row][last_played_column+1] + self.board[last_played_row][last_played_column+2]) == trio_token:
                                num_trios += 1
                                found_trio = True
                                break
                        except IndexError:
                            pass
                        try:
                            # se
                            if (self.board[last_played_row][last_played_column] + self.board[last_played_row+1][last_played_column+1] + self.board[last_played_row+2][last_played_column+2]) == trio_token:
                                num_trios += 1
                                found_trio = True
                                break
                        except IndexError:
                            pass
                        try:
                            # s
                            if (self.board[last_played_row][last_played_column] + self.board[last_played_row+1][last_played_column] + self.board[last_played_row+1][last_played_column]) == trio_token:
                                num_trios += 1
                                found_trio = True
                                break
                        except IndexError:
                            continue
                    if found_trio:
                        break
        elif last_played_letter == 'O':
            # check all lines centered on this cell
            for row in range(self.board_size):
                    for column in range(self.board_size):
                        try:
                            # n-s
                            if (self.board[last_played_row-1][last_played_column] + self.board[last_played_row][last_played_column] + self.board[last_played_row+1][last_played_column]) == trio_token:
                                num_trios += 1
                        except IndexError:
                            pass
                        try:
                            # w-e
                            if (self.board[last_played_row][last_played_column-1] + self.board[last_played_row][last_played_column] + self.board[last_played_row][last_played_column+1]) == trio_token:
                                num_trios += 1
                        except IndexError:
                            pass
                        try:
                            # sw-ne
                            if (self.board[last_played_row+1][last_played_column-1] + self.board[last_played_row][last_played_column] + self.board[last_played_row-1][last_played_column+1]) == trio_token:
                                num_trios += 1
                        except IndexError:
                            pass
                        try:
                            # nw-se
                            if (self.board[last_played_row-1][last_played_column-1] + self.board[last_played_row][last_played_column] + self.board[last_played_row+1][last_played_column+1]) == trio_token:
                                num_trios += 1
                        except IndexError:
                            continue
        if num_trios > 0:
            if self.current_player == 'P1':
                self.p2_score += num_trios
            elif self.current_player == 'P2':
                self.p2_score += num_trios
            return (True, num_trios)
        return (False, num_trios)
    
    def board_full(self):
        for row in range(self.board_size):
            for column in range(self.board_size):
                if self.board[row][column] == ' ':
                    return False
        return True

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

    def new_game(self,):
        """Starts a new game."""
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
