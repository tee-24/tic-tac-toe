import commons
import oneplayer
import twoplayer
import emoji
from colorama import Fore, Back, Style


    
def run_game():
    # Intro
    print(Fore.MAGENTA + emoji.emojize('\nHello! Welcome to Tic Tac Toe :grinning_face_with_big_eyes:'))
    print(Style.RESET_ALL)

    print('Instructions:')
    print('First to get 3 in a row wins!')
    # Empty line
    print()
    # Get number of players
    player_number = commons.get_num_of_players()

    if player_number == 1:
        # Start one player game
        oneplayer.one_player_game()
    else:
        # Start two player game
        twoplayer.two_player_game()


run_game()



