from sos_game import SOSGame
from tkinter import *
from tkinter import ttk

window = Tk()
window.title('SOS Game')

# create test variables for gui
test_board_size = 4
test_game_mode = 'simple'
test_vs_computer = False

# create control variables for gui
gui_gamemode = IntVar

# create SOSGame object
game = SOSGame(test_board_size, test_game_mode, test_vs_computer)




# create Label for current player
label = Label(text=(game.get_current_player() + '\'s turn'), font=('Courier New', 40))
label.pack(side='top')

# create Frame for window
frame = Frame(window)
frame.pack()


# initialize array for game board
gui_board = [[' ' for x in range(game.get_board_size())] for y in range(game.get_board_size())]

def gui_create_board(game, input_board):
    """Create a board in the GUI"""
    input_board = [[' ' for x in range(game.get_board_size())] for y in range(game.get_board_size())]
    for row in range(game.get_board_size()):
        for column in range(game.get_board_size()):
            gui_board[row][column] = Button(frame, text=game.get_cell(row, column), font=('Courier New',40),
                                    width=5, height=2,
                                    command= lambda row=row, col=column: gui_move(game, row,col))
            gui_board[row][column].grid(row=row,column=column)

def gui_reset():
    """Reset both the GUI board and the game board"""
    game.new_game()
    gui_create_board(game, gui_board)

def gui_move(game, row, column):
    """Make a move and display it in the GUI"""
    if gui_board[row][column]['text'] == ' ':
        gui_board[row][column]['text'] = game.get_current_player_piece()
        game.make_move(row, column)
        label.config(text=(game.get_current_player() + '\'s turn'))

def gui_change_gamemode(game):
    """Change the game mode"""

# create new game button
reset_button = Button(text='restart', font=('Courier New',20), command=gui_reset)
reset_button.pack(side='bottom')

# create radio button to change game mode
game_mode_radiobutton = Radiobutton()
game_mode_radiobutton.pack(side='left', padx=50, pady=50, before=frame)

# create radio button to play against computer
vs_computer_radiobutton = Radiobutton()
vs_computer_radiobutton.pack(side='right', padx=50, pady=50, before=frame)


# create board
gui_create_board(game, gui_board)

# main gui loop
window.mainloop()