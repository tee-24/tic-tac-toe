from colorama import Fore, Back, Style
import emoji

# Global variables
Board = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}

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

def display_board(Board):
    """
    Print out the game board
    """
    print(f' {Board[1]} | {Board[2]} | {Board[3]}')
    print(f' {Board[4]} | {Board[5]} | {Board[6]}')
    print(f' {Board[7]} | {Board[8]} | {Board[9]}')


def check_tie(Board):
  """
  Will return True if the board is full 
  or will return False if the board is not full
  """

  for i in range(1,10):
    if Board[i] not in ['X','O']:
        return False
         
    return True


def play_again():
    """
    Starts game again if user chooses 'yes'
    and ends the game if user chooses 'no
    """

    answer = input('Do you want to play again? ').capitalize()
    while answer not in ['Y', 'N', 'Yes', 'No']:
        print("I'm sorry, I don't understand")
        answer = input('Please type Yes or No: ').capitalize()

    if answer in ['Y', 'Yes']:
        print("Great, let's play again!")
    else:
        print(Fore.MAGENTA + emoji.emojize('\nThanks for playing! :grinning_face_with_big_eyes:\n'))
        exit()