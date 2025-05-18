from sos_game import SOSGame
from tkinter import *
from tkinter import ttk

window = Tk()
window.title('SOS Game')

# create test variables for gui
test_board_size = 4
test_gamemode = 0
test_vs_computer = False

# create control variables for gui
# gui_gamemode: int; 0 for simple, 1 for general
# gui_vs_computer: int; 0 for vs player, 1 for vs computer
# gui_vs_computer: int
gui_gamemode = IntVar()
gui_vs_computer = IntVar()
gui_board_size = IntVar(value=3)

# create SOSGame object
game = SOSGame(gui_board_size.get(), test_gamemode, test_vs_computer)

# create Label to display current player's turn and score
gui_turn = Label(text=f'{game.get_current_player()}\'s turn', font=('Courier New', 40))
gui_turn.pack(side='top')

# create Label to display scores
player1_score = 0
player2_score = 0
gui_scoreboard = Label(text=f'P1 score: {player1_score}\nP2 score: {player2_score}', font=('Courier New', 20))
gui_scoreboard.pack(side='top')

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
def gui_change_gamemode():
    """Change the game mode"""
    game.set_gamemode(gui_gamemode.get())
gamemode_simple_radiobutton = Radiobutton(variable=gui_gamemode, value=0, text='Simple game', cursor='hand2', command=gui_change_gamemode)
gamemode_simple_radiobutton.pack(side='left', padx=10, before=frame)
gamemode_general_radiobutton = Radiobutton(variable=gui_gamemode, value=1, text='General game', cursor='hand2', command=gui_change_gamemode)
gamemode_general_radiobutton.pack(side='left', padx=10, before=frame)

# create radio button to play against computer
vs_computer_no_radiobutton = Radiobutton(variable=gui_vs_computer, value=0, text='Versus player')
vs_computer_no_radiobutton.pack(side='right', padx=10, before=frame)
vs_computer_yes_radiobutton = Radiobutton(variable=gui_vs_computer, value=1, text='Versus computer')
vs_computer_yes_radiobutton.pack(side='right', padx=10, before=frame)

# initialize array for game board
gui_board = [[' ' for x in range(24)] for y in range(24)]

def gui_create_board(input_game, input_board, input_turn_indicator, p1_score, p2_score):
    """Create a board in the GUI"""
    input_board = [[' ' for x in range(game.get_board_size())] for y in range(game.get_board_size())]
    for row in range(game.get_board_size()):
        for column in range(game.get_board_size()):
            gui_board[row][column] = Button(frame, text=input_game.get_cell(row, column), font=('Courier New',40),
                                    
                                    command= lambda row=row, col=column, turn_indicator=input_turn_indicator, p1score=p1_score, p2score=p2_score: gui_move(input_game, row, col, turn_indicator, p1score, p2score))
            gui_board[row][column].grid(row=row,column=column, sticky='nsew')

def gui_reset():
    """Reset both the GUI board and the game board"""
    for child in frame.winfo_children():
        child.destroy()
    game.set_board_size(int(board_size_spinbox.get()))
    game.set_gamemode(gui_gamemode.get())
    game.set_vs_computer(gui_vs_computer.get())
    game.new_game()
    gui_scoreboard.config(text=f'P1 score: {player1_score}\nP2 score: {player2_score}')
    gui_turn.config(text=f'{game.get_current_player()}\'s turn')
    gui_create_board(game, gui_board, gui_turn, player1_score, player2_score)

def coconut():
     print('coconut.jpeg')
def freeze_board(frame):
    for child in frame.winfo_children():
                    child.configure(command=coconut)

def gui_move(game, row, column, turn_indicator, p1_score, p2_score):
    """Make a move and display it in the GUI, then check for a winner"""
    if gui_board[row][column]['text'] == ' ':
        gui_board[row][column]['text'] = game.get_current_player_piece()
        last_letter = game.get_current_player_piece()
        print(last_letter)
        last_player = game.get_current_player()
        game.make_move(row, column)
        print(f'Gamemode: {game.get_gamemode()}')
        check_trio_tuple = game.check_trios(last_letter, row, column)
        print(check_trio_tuple)
        if check_trio_tuple[0]:
            # update scores
            print(f'Last player: {last_player}')
            if last_player == 'P1':
                print(check_trio_tuple[1])
                p1_score += check_trio_tuple[1]
                print(f'P1 score: {p1_score}\nP2 score: {p2_score}')
                gui_scoreboard.configure(text=f'P1 score: {p1_score}\nP2 score: {p2_score}', font=('Courier New', 20))
                gui_scoreboard.update()
            elif last_player == 'P2':
                print(check_trio_tuple[1])
                p2_score += check_trio_tuple[1]
                print(f'P1 score: {p1_score}\nP2 score: {p2_score}')
                gui_scoreboard.configure(text=f'P1 score: {p1_score}\nP2 score: {p2_score}', font=('Courier New', 20))
                gui_scoreboard.update()

            # win the game in a simple game
            if game.get_gamemode() == 0:
                print('foo2')
                turn_indicator.configure(text=f'{last_player} wins!')
                freeze_board(frame)
                window.update_idletasks()
                return
            # if general game:
            elif game.get_gamemode() == 1:
                #if board is full, find the winner
                if game.board_full():
                    if p1_score > p2_score:
                        gui_turn.configure(text='P1 wins!')
                        freeze_board(frame)
                    elif p2_score > p1_score:
                        gui_turn.configure(text='P2 wins!')
                        freeze_board(frame)
                    return

        if game.board_full():
             turn_indicator.configure(text=f'It\'s a tie!')
             freeze_board(frame)
             window.update_idletasks()

        turn_indicator.config(text=(game.get_current_player() + '\'s turn'))
        
    



# create new game button
reset_button = Button(text='restart', font=('Courier New',20), command=gui_reset)
reset_button.pack(side='top', pady=10, before=frame)

# create board
gui_create_board(game, gui_board, gui_turn, player1_score, player2_score)

window.mainloop()