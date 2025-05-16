from sos_game import SOSGame

if __name__ == '__main__':

    test_board_size = 3
    test_game_mode = 'simple'
    test_vs_computer = False
    test_game = SOSGame(test_board_size, test_game_mode, test_vs_computer)

    test_game.print_board()

    while True:
        user_row = int(input('P1 turn\nEnter row pos:'))
        user_col = int(input('\nEnter column pos:'))

        test_game.make_move(user_row, user_col)

        test_game.print_board()

       
        
        
        break