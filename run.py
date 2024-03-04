# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Get the player name
# Display Board
# Ask for user choice
# Check for winner
# Is board full

board_place = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}

def run_game():

    get_user_name()

    marker = get_user_marker()

    display_board(board_place)

    board_place[player_choice()] = marker

    display_board(board_place)
    




def get_user_name():
    """
    Get the name of the player
    """

    player = input('What is your name? ').capitalize()
    print(f'Hi {player}! Welcome to Tic Tac Toe')

def get_user_marker():
    """
    """

    choice = input('Would you like to be X or O? ').upper()
    while choice not in ['X','O']:
        print('Invalid choice, please choose X or O')
        choice = input('Would you like to be X or O? ').upper()

    return choice 


def display_board(board_place):
    """
    Print out the game board
    """

    print(f' {board_place[1]} | {board_place[2]} | {board_place[3]}')
    print(f' {board_place[4]} | {board_place[5]} | {board_place[6]}')
    print(f' {board_place[7]} | {board_place[8]} | {board_place[9]}')


def player_choice():

    position = int(input('Where would you like to play? '))
    while position not in board_place:
        print('Invalid choice, please choose a number from 1-9')
        position = int(input('Where would you like to play? '))

    while board_place[position]=='X' or board_place[position]=='O':
        print('That spot has been taken, please choose another number')
        position = int(input('Where would you like to play? '))


    return position 

def computer_choice():

    position = int(input('Where would you like to play? /n'))
    while position not in range(1,10):
        print('/nInvalid choice, please choose a number from 1-9')
        position = int(input('Where would you like to play? '))

    return position 

board_place[7] = 'X'
player_choice()