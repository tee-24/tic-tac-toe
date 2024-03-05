# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Get the player name
# Display Board
# Ask for user choice
# Check for winner
# Is board full

board_place = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}
play_game = True


def place_marker(board_place, position):
    """
    Place the marker on the board and display the board
    """

    board_place[position] = marker
    display_board(board_place)

def get_user_name():
    """
    Get the name of the player
    """

    player = input('What is your name? ').capitalize()
    print(f'Hi {player}! Welcome to Tic Tac Toe')


def get_user_marker():
    """
    Get the markers for Player 1 and Player 2
    """

    choice = ''

    while choice not in ['X','O']:
        choice = input('Would you like to be X or O? ').upper()

        if choice not in ['X','O']:
            print('Invalid choice, please choose X or O')

    if choice == 'X':
        player1 = 'X'
        player2 = 'O'
        print('Player 1 is X')           
        print('Player 2 is O')
    else:
        player1 = 'O'
        player2 = 'X'
        print('Player 1 is O')
        print('Player 2 is X')

    return player1, player2 


def display_board(board_place):
    """
    Print out the game board
    """

    print(f' {board_place[1]} | {board_place[2]} | {board_place[3]}')
    print(f' {board_place[4]} | {board_place[5]} | {board_place[6]}')
    print(f' {board_place[7]} | {board_place[8]} | {board_place[9]}')


def player_choice():

    position = ''

    while position not in board_place or board_place[position] in ['X', 'O']:
        position = int(input('Where would you like to play? '))

        if position not in board_place:
            print('Invalid choice, please choose a number from 1-9')

        elif board_place[position] in ['X', 'O']:
            print('That spot has been taken, please choose another number')

            # add argument for isdigit()

    return position 

def computer_choice():

    position = int(input('Where would you like to play? /n'))
    while position not in range(1,10):
        print('/nInvalid choice, please choose a number from 1-9')
        position = int(input('Where would you like to play? '))

    return position 

def check_winner():
    # Horizontal wins
    if (board_place[1] == board_place[2] == board_place[3]) or (board_place[4] == board_place[5] == board_place[6]) or (board_place[7] == board_place[8] == board_place[9]):
        print('game over')
    # Verical wins
    elif (board_place[1] == board_place[4] == board_place[7]) or (board_place[2] == board_place[5] == board_place[8]) or (board_place[3] == board_place[6] == board_place[9]):
        print('game over')
    # Diagonal wins
    elif (board_place[1] == board_place[5] == board_place[9]) or (board_place[3] == board_place[5] == board_place[7]):
        print('game over')

def check_tie():
    """
    Checks if the board is full
    """


def play_again():
    """
    Ask if player would like to play again
    """

    answer = input('Do you want to play again? ').capitalize()
    while answer not in ['Y', 'N', 'Yes', 'No']:
        print("I'm sorry, I don't understand")
        answer = input('Please type Yes or No: ').capitalize()

    if answer in ['Y', 'Yes']:
        print('Yay!')
    else:
        print('Thanks for playing!')

    return answer 

while play_game == True:

    get_user_name()

    marker = get_user_marker()

    display_board(board_place)

    player_choice()

    place_marker(board_place, player_choice())