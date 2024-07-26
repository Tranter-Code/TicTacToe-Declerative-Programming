#from typing import NoReturn
from DataModel.Players import *
from DataModel.Grid import *
from DataModel.Menu import *
import sys
import time

#def assert_never(value: NoReturn) -> NoReturn:
#    assert False, f'Unhandled value: {value} ({type(value).__name__})'

#def do_something_with_token(t:Token) -> None:
#    if isinstance(t, Token):
#        match t:
#            case X():
#                print("X") 
#            case O():
#                print("O")
#    else:
#        assert_never(t)


"""
Easy = random cell form empty cells remaining
Normal = % chance of activating minimax vs choosing random cell from empty cells
Hard = MiniMax
"""

def gameplay_loop(players: Players, grid: Grid) -> None:
    print(players[0][1] + "'s turn.")
    display_grid(grid)
    match players[0][0]:
        case CPU():
            time.sleep(2)
            new_grid = cpu_turn(players, grid)
        case Human():
            new_grid = take_turn(players, grid)
    os.system('clear')
    if check_for_winner(new_grid) == True:
        print(players[0][1] + " wins!")
        display_grid(new_grid)
        return None 
    elif check_for_draw(new_grid) == True:
        print("It's a draw!")
        display_grid(new_grid)
        return None
    next_player_order = swap_player_order(players)
    return gameplay_loop(next_player_order, new_grid)

def single_player_game_setup() -> None:
    players = set_up_player_and_cpu()
    grid = init_grid()
    gameplay_loop(players, grid)

def two_player_game_setup() -> None:
    players = set_up_two_players()
    random_player_order = randomise_player_order(players)
    grid = init_grid()
    gameplay_loop(random_player_order, grid)

def run_main_menu() -> None:
    display_main_menu()
    menu_result = read_menu_choice()
    match menu_result:
        case MenuOption.StartSinglePlayer:
            return single_player_game_setup()
        case MenuOption.StartTwoPlayer:
            return two_player_game_setup()
        case MenuOption.ExitGame:
            sys.exit(0)

  
if __name__ == "__main__":
    run_main_menu()
    sys.exit(0)