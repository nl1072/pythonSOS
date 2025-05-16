from sos_game import SOSGame

if __name__ == '__main__':

    console_board_size = 3
    console_game_mode = 'simple'
    console_vs_computer = False
    console_game = SOSGame(console_board_size, console_game_mode, console_vs_computer)

    console_game.print_board()

    while True:
        user_row = int(input('\n' + console_game.get_current_player() + '\'sturn\nEnter row pos:'))
        user_col = int(input('\nEnter column pos:'))

        if user_row == -1:
            break
        console_game.make_move(user_row, user_col)

        console_game.print_board()

       
        
        
        