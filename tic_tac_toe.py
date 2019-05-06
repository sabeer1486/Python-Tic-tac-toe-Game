# Python-Tic-tac-toe-Game


# ------global valriable go here-----

#this is our game's board
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

#this will tell who is the current player
current_player = 'X'

#this will tell us game is still going or not
game_still_going = True

#winner will be none when game is still going or game will go tie
winner = None


#this functin call will start the game
def play_game():
    global game_still_going

    display_board()

    while game_still_going:

        handle_player(current_player)

        check_for_game_over()

        flip_player()
    if winner == 'X' or winner == 'O':
        print(winner, " won")
    else:
        print('tie !')

#display's the board on screen
def display_board():
    print('\n')
    print(board[0]+ ' | ' + board[1] +' | '+ board[2]+ '              1 | 2 | 3')
    print(board[3]+ ' | ' + board[4] +' | '+ board[5]+ '              4 | 5 | 6')
    print(board[6]+ ' | ' + board[7] +' | '+ board[8]+ '              7 | 8 | 9')
    print('\n')


#this will handle the player
def handle_player(player):
    print(player, "'s turn")
    position = input('Enter position from 1-9 : ')
    valid = False
    while not valid:
        while position not in ['1', '2', '3', '4', '4', '5', '6', '7', '8', '9']:
            position = input('Enter position from 1-9 : ')
        position = int(position) - 1
        if board[position] == '-':
            board[position] = player
            valid = True
        else:
            print('you cannot go there try again')
    display_board()
        
#check's the game is still going or not
def check_for_game_over():
    check_for_winner()
    check_for_tie()

#check's for winner row, col and diagonal wise
def check_for_winner():
    global winner
    row_winner = check_for_rows()
    col_winner = check_for_cols()
    dia_winner = check_for_diagonals()
    if row_winner:
        winner = row_winner
    elif col_winner:
        winner = col_winner
    elif dia_winner:
        winner = dia_winner
    
#check for winner in rows
def check_for_rows():
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None

#check for winner in columns
def check_for_cols():
    global game_still_going
    col_1 = board[0] == board[3] == board[6] != '-'
    col_2 = board[1] == board[4] == board[7] != '-'
    col_3 = board[2] == board[5] == board[8] != '-'
    if col_1 or col_2 or col_3:
        game_still_going = False
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    else:
        return None

#check for winner in diagonals
def check_for_diagonals():
    global game_still_going
    dia_1 = board[0] == board[4] == board[8] != '-'
    dia_2 = board[2] == board[4] == board[6] != '-'
    if dia_1 or dia_2:
        game_still_going = False
    if dia_1:
        return board[0]
    elif dia_2:
        return board[2]
    else:
        return None

#tell's game is tied if no space in the board
def check_for_tie():
    global game_still_going
    if '-' not in board:
        game_still_going = False

#changes the turn of the player
def flip_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player= 'X'

#game start function call
play_game()

#if you want to play game again
def play_again():
    # initialise all golbal variable to starting values

    global winner, game_still_going, current_player, board

    winner = None

    game_still_going = True

    current_player = 'X'

    board = ['-', '-', '-',
             '-', '-', '-',
             '-', '-', '-']

    #Asks user to yes or no
    decession = input('want to play again ? (Y/N) : ').upper()
    while decession not in ['Y', 'N']:
        decession = input('want to play again ? (Y/N) : ').upper()
    if decession == 'Y':
        return True
    elif decession == 'N':
        return False

want_to_play = True
while want_to_play:

    #gets decession from the play_again()
    repeat_decession = play_again()

    #if repeat_decession is true game start again
    if repeat_decession:
        play_game()

    #if repeat_decession is false says byer
    else:
        print('bye')
        want_to_play = False
