from sos_game import SOSGame
from tkinter import *
from tkinter import ttk

window = Tk()
window.title('SOS Game')

# create test variables for gui
test_board_size = 4
test_gamemode = 'simple'
test_vs_computer = False

# create control variables for gui
gui_gamemode = IntVar()
gui_vs_computer = IntVar()
gui_board_size = IntVar(value=3)

# create SOSGame object
game = SOSGame(gui_board_size.get(), test_gamemode, test_vs_computer)


# create Label to display current player's turn
gui_turn = Label(text=(game.get_current_player() + '\'s turn'), font=('Courier New', 40))
gui_turn.pack(side='top')

# create spinbox to select board size
board_size_label = Label(text='Board size\nmin. 3, max.24', font=('Arial', 10))
board_size_label.pack(side='top')
board_size_spinbox = Spinbox(textvariable=gui_board_size, from_=3, to=24, increment=1)
board_size_spinbox.pack(side='top')


# create Frame for window
frame = Frame(window)
frame.pack()
frame.columnconfigure(tuple(range(30)), weight=1)
frame.rowconfigure(tuple(range(30)), weight=1)

# create radio buttons to change game mode
gamemode_simple_radiobutton = Radiobutton(variable=gui_gamemode, value=0, text='Simple game', cursor='hand2')
gamemode_simple_radiobutton.pack(side='left', padx=10, before=frame)
gamemode_general_radiobutton = Radiobutton(variable=gui_gamemode, value=1, text='General game', cursor='hand2')
gamemode_general_radiobutton.pack(side='left', padx=10, before=frame)

# create radio button to play against computer
vs_computer_no_radiobutton = Radiobutton(variable=gui_vs_computer, value=0, text='Versus player')
vs_computer_no_radiobutton.pack(side='right', padx=10, before=frame)
vs_computer_yes_radiobutton = Radiobutton(variable=gui_vs_computer, value=1, text='Versus computer')
vs_computer_yes_radiobutton.pack(side='right', padx=10, before=frame)

# initialize array for game board
gui_board = [[' ' for x in range(24)] for y in range(24)]

def gui_create_board(input_game, input_board, input_turn_indicator):
    """Create a board in the GUI"""
    input_board = [[' ' for x in range(game.get_board_size())] for y in range(game.get_board_size())]
    for row in range(game.get_board_size()):
        for column in range(game.get_board_size()):
            gui_board[row][column] = Button(frame, text=input_game.get_cell(row, column), font=('Courier New',40),
                                    
                                    command= lambda row=row, col=column, turn_indicator=input_turn_indicator: gui_move(input_game, row, col, turn_indicator))
            gui_board[row][column].grid(row=row,column=column, sticky='nsew')

def gui_reset():
    """Reset both the GUI board and the game board"""
    for child in frame.winfo_children():
        child.destroy()
    game.set_board_size(int(board_size_spinbox.get()))
    game.set_gamemode(gui_gamemode.get())
    game.set_vs_computer(gui_vs_computer.get())
    game.new_game()
    gui_create_board(game, gui_board, gui_turn)

def gui_move(game, row, column, turn_indicator):
    """Make a move and display it in the GUI"""
    if gui_board[row][column]['text'] == ' ':
        gui_board[row][column]['text'] = game.get_current_player_piece()
        game.make_move(row, column)
        turn_indicator.config(text=(game.get_current_player() + '\'s turn'))
def gui_change_gamemode(game):
    """Change the game mode"""

# create new game button
reset_button = Button(text='restart', font=('Courier New',20), command=gui_reset)
reset_button.pack(side='top', pady=10, before=frame)

# create board
gui_create_board(game, gui_board, gui_turn)

window.mainloop()