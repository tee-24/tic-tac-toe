from colorama import Fore, Back, Style
import emoji
import oneplayer

# Global variables
board = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}


def get_num_of_players():

    answer = 0

    while answer not in [1, 2]:
        try:
            answer = int(input('1 or 2 players? '))
        except ValueError:
            print(Fore.RED + '\nInvalid choice, please choose 1 or 2')
            print(Style.RESET_ALL)
            continue

        if answer not in [1, 2]:
            print(Fore.RED + '\nInvalid choice, please choose 1 or 2')
            print(Style.RESET_ALL)
    
    return answer

def display_board(board):
    """
    Print out the game board
    """
    print(f' {board[1]} | {board[2]} | {board[3]}')
    print(f' {board[4]} | {board[5]} | {board[6]}')
    print(f' {board[7]} | {board[8]} | {board[9]}')


def check_tie(board):
    """
    Will return True if the board is full 
    or will return False if the board is not full
    """

    for key in board:
        if board[key].isdigit():
            return False
    return True




def reset_board(board):
    """
    Resets the board to default
    """
    for spot in range(1,10):
        board[spot] = str(spot)