"""Milestone Project"""
from IPython.display import clear_output
import random

from notebook.notebookapp import raw_input


def display_board():
    """
    This function prints out the board so the numpad can be used as a reference
    :return:
    """
    clear_output ()
    print ( '\n   |   |' )
    print ( ' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] )
    print ( '   |   |' )
    print ( '-----------' )
    print ( '   |   |' )
    print ( ' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] )
    print ( '   |   |' )
    print ( '-----------' )
    print ( '   |   |' )
    print ( ' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] )
    print ( '   |   |\n' )
    return board


def player_input():
    """
    KEEP ASKING PLAYER 1 to choose X or O
    ASSIGN PLAYER 2, the opposite marker
    :return: OUTPUT = (Player 1 marker, Player 2 marker)
    """
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input ( 'Player 1, choose X or O: ' ).upper ()
    player_one = marker
    if player_one == 'X':
        player_2 = 'O'
    else:
        player_2 = 'X'
    return player_one, player_2


def place_maker(boards, marker, positions):
    """
    :param boards:
    :param marker:
    :param positions:
    :return:
    """
    boards[positions] = marker


def win_check(boards, mark):
    """
    WIN TIC TAC TOE?
    ALL ROWS, and c heck to see if they all share the same marker?
    ALL COLUMNS, check to see if marker matches
    2 diagonals, check to see match
    :param boards:
    :param mark:
    :return:
    """
    return ((boards[7] == boards[8] == boards[9] == mark) or
            (boards[4] == boards[5] == boards[6] == mark) or
            (boards[1] == boards[2] == boards[3] == mark) or
            (boards[7] == boards[4] == boards[1] == mark) or
            (boards[8] == boards[5] == boards[2] == mark) or
            (boards[9] == boards[6] == boards[3] == mark) or
            (boards[7] == boards[5] == boards[3] == mark) or
            (boards[9] == boards[5] == boards[1] == mark))


def choose_first():
    """
    :return:
    """
    flip = random.randint ( 0, 1 )
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(boards, positions):
    """
    :param boards:
    :param positions:
    :return:
    """
    return boards[positions] == ' '


def full_board_check(boards):
    """
    BOARD IS FULL IF WE RETURN TRUE
    :param boards:
    :return:
    """
    return " " not in boards[1:]


def player_choice(mark):
    """
    Set blank game announcement
    :param mark: Get player input
    :return: Show board
    """
    global board, game_state, announce
    announce = ''
    mark = str ( mark )
    ask_player ( mark )
    if win_check ( board, mark ):
        clear_output ()
        display_board ()
        announce = mark + " wins! Congratulations"
        game_state = False
    clear_output ()
    display_board ()
    if full_board_check ( board ):
        announce = "Tie!"
        game_state = False
    return game_state, announce


def replay():
    """
    :return:
    """
    choice = input ( "Play again? Enter Yes or No: " ).upper ()
    return choice == "YES" or choice == "Y"


def reset_board():
    """
    Note: Game will ignore the 0 index
    """
    global board, game_state
    board = [' '] * 10
    game_state = True


def ask_player(mark):
    """
    Asks player where to place X or O marks, checks validity
    :param mark:
    """
    global board
    req = 'Choose where to place your: ' + mark
    while True:
        try:
            choice = int ( raw_input ( req ) )
        except ValueError:
            print ( "Sorry, please input a number between 1-9." )
            continue
        if board[choice] == " ":
            board[choice] = mark
            break
        else:
            print ( "That space isn't empty!" )
            continue


def play_game():
    """
    Sets marks, show board, player X/O turn
    """
    reset_board ()
    global announce
    x = 'X'
    o = 'O'
    while True:
        clear_output ()
        display_board ()
        game_states, announce = player_choice ( x )
        print ( announce )
        if not game_states:
            break
        game_states, announce = player_choice(o)
        print(announce)
        if not game_states:
            break
    rematch = raw_input('Would you like to play again? y/n: ')
    if rematch == 'y':
        play_game()
    else:
        print("Thanks for playing!")


board = [' '] * 10
game_state = True
announce = ''
print ( 'Welcome to Tic Tac Toe!' )
while True:
    player_1_marker, player_2_marker = player_input ()
    turn = choose_first ()
    print ( turn + ' will go first.' )
    play_game = input ( 'Ready to play? y or n?: ' ).upper ()
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == 'Player 1':
            display_board ()
            position = player_choice ( board )
            place_maker ( board, player_1_marker, position )
            if win_check ( board, player_1_marker ):
                display_board ()
                print ( 'PLAYER 1 HAS WON!!' )
                game_on = False
            else:
                if full_board_check ( board ):
                    display_board ()
                    print ( "TIE GAME!" )
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            display_board ()
            position = player_choice ( board )
            place_maker ( board, player_2_marker, position )
            if win_check ( board, player_2_marker ):
                display_board ()
                print ( 'PLAYER 2 HAS WON!!' )
                game_on = False
            else:
                if full_board_check ( board ):
                    display_board ()
                    print ( "TIE GAME!" )
                    game_on = False
                else:
                    turn = 'Player 1'
    if not replay ():
        break
