from sos_game import SOSGame
from tkinter import *
from tkinter import ttk

window = Tk()
window.title('SOS Game')

test_board_size = 4
test_game_mode = 'simple'
test_vs_computer = False
game = SOSGame(test_board_size, test_game_mode, test_vs_computer)

# create label for current player
label = Label(text=(game.get_current_player() + '\'s turn'), font=('Courier New', 40))
label.pack(side='top')

# create new game button
reset_button = Button(text='restart', font=('Courier New',20),
                      command = game.new_game)
reset_button.pack(side='top')

# create frame for window
frame = Frame(window)
frame.pack()

# create board of buttons
gui_board = [['_' for x in range(game.get_board_size())] for y in range(game.get_board_size())]
def gui_move(game, row, column):
    gui_board[row][column]['text'] = game.get_current_player_piece()
    game.make_move(row, column)
    label.config(text=(game.get_current_player() + '\'s turn'))


for row in range(game.get_board_size()):
    for column in range(game.get_board_size()):
        gui_board[row][column] = Button(frame, text=game.get_cell(row, column), font=('Courier New',40),
                                   width=5, height=2,
                                   command= lambda row=row, col=column: gui_move(game, row,col))
        gui_board[row][column].grid(row=row,column=column)
window.mainloop()