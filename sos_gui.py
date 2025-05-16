from sos_game import SOSGame
from tkinter import *
from tkinter import ttk

window = Tk()
window.title('SOS Game')

test_board_size = 4
test_game_mode = 'simple'
test_vs_computer = False

game = SOSGame(test_board_size, test_game_mode, test_vs_computer)
label = Label(text=(game.get_current_player() + '\'s turn'), font=('Courier New', 40))
label.pack(side='top')

reset_button = Button(text='restart', font=('Courier New',20),
                      command = game.new_game)
reset_button.pack(side='top')

frame = Frame(window)
frame.pack()


gui_board = [['_' for x in range(game.get_board_size())] for y in range(game.get_board_size())]
for row in range(game.get_board_size()):
    for col in range(game.get_board_size()):
        gui_board[row][col] = Button(frame, text=game.get_cell(row,col), font=('Courier New',40),
                                   width=5, height=2,
                                   command= lambda row=row, col=col: game.make_move(row,col))
        gui_board[row][col].grid(row=row,column=col)
window.mainloop()