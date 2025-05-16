from sos_game import SOSGame
from tkinter import *
from tkinter import ttk

window = Tk
window.title('SOS Game')


game = SOSGame()
label = Label(text=game.get_current_player() + '\'s turn', font = 'Courier New')