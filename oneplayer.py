import commons
import random
import emoji
import os
from colorama import Fore, Back, Style

# Global variables
board = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}
play_game = True



def get_user_name():
    """
    Get the name of the player
    """
    player = ''

    while len(player) < 3 or not player.isalpha() or len(player) > 10:
        player = input('\nWhat is your name? ').capitalize()

        if player.isalpha() == False:
            print(Fore.RED + 'Name can only contain letters, please try again')
            print(Style.RESET_ALL)
        elif len(player) < 3:
            print(Fore.RED + 'Name must be a minimum of 3 letters, please try again')
            print(Style.RESET_ALL)
        elif len(player) > 10:
            print(Fore.RED + 'Name can only be a maximum of 10 letters, please try again')
            print(Style.RESET_ALL)

    print(f'\nHi {player}!')
    return player

def get_user_marker():
    """
    Get the markers for Player 1 and Player 2
    """
    choice = ''

    while choice not in ['X','O']:
        choice = input('Would you like to be X or O? ').upper()

        if choice not in ['X','O']:
            print(Fore.RED + 'Invalid choice, please choose X or O')
            print(Style.RESET_ALL)

    return choice



def player_choice(user_marker):

    position = ''

    while position not in board or board[position] in ['X', 'O']:
        try:
            position = int(input('Where would you like to play? '))
        except ValueError:
            print(Fore.RED + '\nInvalid choice, please choose a number from 1-9')
            print(Style.RESET_ALL)
            continue

        if position not in board:
            print(Fore.RED + '\nInvalid choice, please choose a number from 1-9')
            print(Style.RESET_ALL)

        elif board[position] in ['X', 'O']:
            print(Fore.BLUE + '\nThat spot has been taken, please choose another number')
            print(Style.RESET_ALL)
    # Place marker on the board
    place_marker(board, position, user_marker, player=True)

    return position 

def computer_choice(computer_marker):

    print("\nComputer's turn...\n")

    choice = 0

    while choice not in board or board[choice] in ['X', 'O']:
        choice = random.randint(1,9)

    place_marker(board, choice, computer_marker, player=False)

    return choice 

def place_marker(board, position, marker, player=None):
    """
    Place the marker on the board 
    and display the board
    """
    board[position] = marker
    commons.display_board(board)
    # Check for winner
    check_winner(player)

def check_winner(player):
    # Horizontal wins
    if (
        board[1] == board[2] == board[3]
        ) or (
            board[4] == board[5] == board[6]
            ) or (
                board[7] == board[8] == board[9]):
        # If user wins
        if player:
            print(Fore.GREEN + emoji.emojize('\nCongrats, you won! :party_popper:'))
            print(Style.RESET_ALL)
        else:
            print(Fore.BLUE + emoji.emojize('\nOh no! You lost :pensive_face:'))
            print('The computer wins')
            print(Style.RESET_ALL)
        # Replay
        play_again()
    # Vertical wins
    elif (
        board[1] == board[4] == board[7]
        ) or (
            board[2] == board[5] == board[8]
            ) or (
                board[3] == board[6] == board[9]):
        # If user wins
        if player:
            print(Fore.GREEN + emoji.emojize('\nCongrats, you won! :party_popper:'))
            print(Style.RESET_ALL)
        else:
            print(Fore.BLUE + emoji.emojize('\nOh no! You lost :pensive_face:'))
            print('The computer wins')
            print(Style.RESET_ALL)
        # Replay
        play_again()
    # Diagonal wins
    elif (
        board[1] == board[5] == board[9]
        ) or (
            board[3] == board[5] == board[7]):
        # If user wins
        if player:
            print(Fore.GREEN + emoji.emojize('\nCongrats, you won! :party_popper:'))
            print(Style.RESET_ALL)
        else:
            print(Fore.BLUE + emoji.emojize('\nOh no! You lost :pensive_face:'))
            print('The computer wins')
            print(Style.RESET_ALL)
        # Replay
        play_again()
    elif commons.check_tie(board) is True:
        print("It's a tie!")
        # Replay
        play_again()
        
def play_again():
    """
    Starts game again if user chooses 'yes'
    and ends the game if user chooses 'no
    """

    answer = input('Do you want to play again? ').capitalize()
    while answer not in ['Y', 'N', 'Yes', 'No']:
        print("I'm sorry, I don't understand")
        answer = input('Please type Yes or No: ').capitalize()
    # If user chooses yes
    if answer in ['Y', 'Yes']:
        print("Great, let's play again!")
        one_player_game()
    # If user chooses no
    else:
        print(Fore.MAGENTA + emoji.emojize('\nThanks for playing! :grinning_face_with_big_eyes:\n'))
        exit()

def one_player_game():

    user_marker = get_user_marker()
    # Determine computer marker based on user's marker
    if user_marker == 'X':
        computer_marker = 'O'
    else:
        computer_marker = 'X'
    # Reset the board
    commons.reset_board(board) 
    # Display the board
    commons.display_board(board)

    while play_game == True:
        
        print()
        # Where the user wants to play
        player_choice(user_marker)
        # Where the computer wants to play
        computer_choice(computer_marker)
        # Check for tie
        # tie = commons.check_tie(Board)
        # if tie:
        #     print("It's a tie!")
        #     exit()
        # else:
        #     continue
        
