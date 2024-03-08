
# Is board full
import commons
import emoji
import random
from colorama import Fore, Back, Style

# Global variables
Board = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}
play_game = True


def get_player1_name():
    """
    Get the name of Player 1
    """
    player1 = ''

    while len(player1) < 3 or not player1.isalpha() or len(player1) > 10:
        player1 = input('\nPlayer 1, enter your name: ').capitalize()

        if player1.isalpha() == False:
            print('Name can only contain letters, please try again')
        elif len(player1) < 3:
            print('Name must be a minimum of 3 letters, please try again')
        elif len(player1) > 10:
            print('Name can only be a maximum of 10 letters, please try again')

    print(f'{player1} is Player 1')

    return player1

def get_player2_name():
    """
    Get the name of Player 2
    """
    player2 = ''

    while len(player2) < 3 or not player2.isalpha() or len(player2) > 10:
        player2 = input('\nPlayer 2, enter your name: ').capitalize()

        if player2.isalpha() == False:
            print(Fore.RED + 'Name can only contain letters, please try again')
            print(Style.RESET_ALL)
        elif len(player2) < 3:
            print(Fore.RED + 'Name must be a minimum of 3 letters, please try again')
            print(Style.RESET_ALL)
        elif len(player2) > 10:
            print(Fore.RED + 'Name can only be a maximum of 10 letters, please try again')
            print(Style.RESET_ALL)
        
    print(f'{player2} is Player 2')

    return player2


def get_player1_marker(player1, player2):
    """
    Get the markers for Player 1
    """

    choice = ''

    while choice not in ['X','O']:
        choice = input(f'\n{player1}, would you like to be X or O? ').upper()

        if choice not in ['X','O']:
            print('Invalid choice, please choose X or O')

    if choice == 'X':
        print(f'{player1} is X')           
        print(f'{player2} is O')
    else:
        print(f'{player1} is O')
        print(f'{player2} is X')

    return choice

def player1_choice(player1_marker, player1):

    position = ''

    while position not in Board or Board[position] in ['X', 'O']:
        try:
            position = int(input(f'Where would you like to play {player1}? '))
        except ValueError:
            print('Invalid choice, please choose a number from 1-9')
            continue

        if position not in Board:
            print('Invalid choice, please choose a number from 1-9')

        elif Board[position] in ['X', 'O']:
            print('That spot has been taken, please choose another number')

    place_marker(Board, position, player1_marker, player=True)

    return position 

def player2_choice(player2_marker, player2):

    position = ''

    while position not in Board or Board[position] in ['X', 'O']:
        try:
            position = int(input(f'Where would you like to play {player2}? '))
        except ValueError:
            print('Invalid choice, please choose a number from 1-9')
            continue

        if position not in Board:
            print('Invalid choice, please choose a number from 1-9')

        elif Board[position] in ['X', 'O']:
            print('That spot has been taken, please choose another number')

    place_marker(Board, position, player2_marker, player=False)

    return position 

def place_marker(Board, position, marker, player=None):
    """
    Place the marker on the board 
    and display the board
    """
    Board[position] = marker
    commons.display_board(Board)
    # Check for winner
    check_winner(player)

def check_winner(player):
    # Horizontal wins
    if (
        Board[1] == Board[2] == Board[3]
        ) or (
            Board[4] == Board[5] == Board[6]
            ) or (
                Board[7] == Board[8] == Board[9]):
        # If Player 1 wins
        if player:
            print(Fore.GREEN + emoji.emojize(f'\nCongrats {player}, you won! :party_popper:'))
            print(Fore.BLUE + emoji.emojize(f'\nBetter luck next time {player}'))
            print(Style.RESET_ALL)
        else:
            print(Fore.GREEN + emoji.emojize(f'\nCongrats {player}, you won! :party_popper:'))
            print(Fore.BLUE + emoji.emojize(f'\nBetter luck next time {player}'))
            print(Style.RESET_ALL)
        # Replay
        commons.play_again()
    # Vertical wins
    elif (
        Board[1] == Board[4] == Board[7]
        ) or (
            Board[2] == Board[5] == Board[8]
            ) or (
                Board[3] == Board[6] == Board[9]):
        # If Player 1 wins
        if player:
            print(Fore.GREEN + emoji.emojize(f'\nCongrats {player}, you won! :party_popper:'))
            print(Fore.BLUE + emoji.emojize(f'\nBetter luck next time {player}'))
            print(Style.RESET_ALL)
        else:
            print(Fore.GREEN + emoji.emojize(f'\nCongrats {player}, you won! :party_popper:'))
            print(Fore.BLUE + emoji.emojize(f'\nBetter luck next time {player}'))
            print(Style.RESET_ALL)
        # Replay
        commons.play_again()
    # Diagonal wins
    elif (
        Board[1] == Board[5] == Board[9]
        ) or (
            Board[3] == Board[5] == Board[7]):
        # If Player 1 wins
        if player:
            print(Fore.GREEN + emoji.emojize(f'\nCongrats {player}, you won! :party_popper:'))
            print(Fore.BLUE + emoji.emojize(f'\nBetter luck next time {player}'))
            print(Style.RESET_ALL)
        else:
            print(Fore.GREEN + emoji.emojize(f'\nCongrats {player}, you won! :party_popper:'))
            print(Fore.BLUE + emoji.emojize(f'\nBetter luck next time {player}'))
            print(Style.RESET_ALL)
        # Replay
        commons.play_again()

def two_player_game():
    
    # Get names of players
    player1 = get_player1_name()
    player2 = get_player2_name()
    # Get Player 1 marker
    player1_marker = get_player1_marker(player1, player2)
    # Determine Player 2 marker based on Player 1 marker
    if player1_marker == 'X':
        player2_marker = 'O'
    else:
        player2_marker = 'X'
    # Empty line
    print()
    # Display board
    commons.display_board(Board)

    while play_game == True:
        print()
        # Where Player 1 wants to play
        player1_choice(player1_marker, player1)
        # Where Player 2 wants to play
        player2_choice(player2_marker, player2)
    


