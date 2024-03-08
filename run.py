# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Get the player name
# Display Board
# Ask for user choice
# Check for winner
# Is board full

import emoji
import random
from colorama import Fore, Back, Style

board_place = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}
play_game = True
turn = 0


def place_marker(board_place, position, marker):
    """
    Place the marker on the board 
    and display the board
    """
    board_place[position] = marker
    display_board(board_place)

    check_winner()

def get_user_name():
    """
    Get the name of the player
    """
    player = ''

    while len(player) < 3 or not player.isalpha():
        player = input('What is your name? ').capitalize()

        if player.isalpha() == False:
            print(Fore.RED + 'Name can only contain letters, please try again')
            print(Style.RESET_ALL)
        elif len(player) < 3:
            print(Fore.RED + 'Name must be a minimum of 3 letters, please try again')
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

def display_board(board_place):
    """
    Print out the game board
    """
    print(f' {board_place[1]} | {board_place[2]} | {board_place[3]}')
    print(f' {board_place[4]} | {board_place[5]} | {board_place[6]}')
    print(f' {board_place[7]} | {board_place[8]} | {board_place[9]}')


def player_choice(user_marker):

    position = ''

    while position not in board_place or board_place[position] in ['X', 'O']:
        try:
            position = int(input('Where would you like to play? '))
        except ValueError:
            print(Fore.RED + '\nInvalid choice, please choose a number from 1-9')
            print(Style.RESET_ALL)
            continue

        if position not in board_place:
            print(Fore.RED + '\nInvalid choice, please choose a number from 1-9')
            print(Style.RESET_ALL)

        elif board_place[position] in ['X', 'O']:
            print(Fore.BLUE + '\nThat spot has been taken, please choose another number')
            print(Style.RESET_ALL)

    place_marker(board_place, position, user_marker)

    return position 

def computer_choice(computer_marker):

    print("\nComputer's turn...\n")

    choice = 0

    while choice not in board_place or board_place[choice] in ['X', 'O']:
        choice = random.randint(1,9)

    place_marker(board_place, choice, computer_marker)

    return choice 

def check_winner():
    # Horizontal wins
    if (
        board_place[1] == board_place[2] == board_place[3]
        ) or (
            board_place[4] == board_place[5] == board_place[6]
            ) or (
                board_place[7] == board_place[8] == board_place[9]):
        print('game over')
        break
    # Vertical wins
    elif (
        board_place[1] == board_place[4] == board_place[7]
        ) or (
            board_place[2] == board_place[5] == board_place[8]
            ) or (
                board_place[3] == board_place[6] == board_place[9]):
        print('game over')
        continue
    # Diagonal wins
    elif (
        board_place[1] == board_place[5] == board_place[9]
        ) or (
            board_place[3] == board_place[5] == board_place[7]):
        print('game over')
        continue

def check_tie(board_place):
  """
  Will return True if the board is full 
  or will return False if the board is not full
  """

  for i in range(1,10):
      if board_place[i] not in ['X','O']:
        return False
        
  return True

def play_again():
    """
    Starts game again if user chooses 'yes'
    and ends the game if user chooses 'no
    """

    answer = input('\nDo you want to play again? ').capitalize()
    while answer not in ['Y', 'N', 'Yes', 'No']:
        print("I'm sorry, I don't understand")
        answer = input('Please type Yes or No: ').capitalize()

    if answer in ['Y', 'Yes']:
        print("Great, let's play again!")
    else:
        print('Thanks for playing!')
        exit()

    return answer 
     
    
def run_game():

    print(emoji.emojize('Hello! Welcome to Tic Tac Toe :grinning_face_with_big_eyes:\n'))

    print('First to get 3 in a row wins!')

    get_user_name()

    user_marker = get_user_marker()
    # Determine computer marker based on user's marker
    if user_marker == 'X':
        computer_marker = 'O'
    else:
        computer_marker = 'X'
    
    print()
    display_board(board_place)

    while play_game == True:
        print()
        # Where the user wants to play
        player_choice(user_marker)
        # Where the computer wants to play
        computer_choice(computer_marker)
    
    play_again()

run_game()
