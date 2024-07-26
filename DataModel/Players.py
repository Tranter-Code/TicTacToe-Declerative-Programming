from typing import Tuple
from DataModel.Token import *
from DataModel.Coord import *
from DataModel.Grid import *
import os

@dataclass(eq=True, frozen=True)
class Human:
    pass

@dataclass(eq=True,frozen=True)
class CPU:
    pass

# let PlayerType = {Human} U {CPU}
PlayerType : TypeAlias = Human | CPU

# let Player = PlayerType X String X Token
Player: TypeAlias = Tuple[PlayerType, str, Token]

# let Players = Player X Player
Players: TypeAlias = Tuple[Player, Player]

# create_player : String x Token -> Player
def create_player(player_type: PlayerType, name: str, tkn: Token) -> Player:
    return (player_type, name, tkn)

# create_player_pair : Player x Player -> Players
def create_players_pair(p1: Player, p2: Player) -> Players:
    return (p1, p2)

# set_up_player : (prompt_message: str X tkn: Token) -> Player
def set_up_player(player_type: Human | CPU, prompt_message: str, tkn: Token) -> Player:
    p_name = input(prompt_message)
    p_tkn = tkn
    os.system('clear')
    return create_player(player_type, p_name, p_tkn)

def set_up_two_players() -> Players:
    p1 = set_up_player(Human(), "Player 1, Please input your name: ", get_token(None))
    p2 = set_up_player(Human(), "Player 2, Please input your name: ", get_token(p1[2]))
    return create_players_pair(p1, p2)

def set_up_player_and_cpu() -> Players:
    p1 = set_up_player(Human(), "Please input your name: ", read_token_input())
    p2 = create_player(CPU(), "CPU", get_token(p1[2]))
    return create_players_pair(p1, p2)

# swap_turns : Players -> Players
# Let swap_turns = lambda(P1,P2) = (P2,P1)
def swap_player_order(players: Players) -> Players:
    return create_players_pair(players[1], players[0])

def randomise_player_order(players: Players) -> Players:
    if random.choice([True, False]):
        return swap_player_order(players)
    else: return players

def take_turn(players: Players, grd: Grid) -> Grid:
    while True:
        turn_tkn = players[0][2]
        coord_result = read_coord_input()
        result_grid = place_token(turn_tkn, coord_result, grd)
        match result_grid:
            case None:
                print("ERROR: Coordinate is already taken. Try again.")
            case _ as Grid:
                return Grid

def cpu_turn(players: Players, grd: Grid) -> Grid:
   while True:
        turn_tkn = players[0][2]
        coord_result = get_random_coord(grd)
        result_grid = place_token(turn_tkn, coord_result, grd)
        match result_grid:
            case None:
                print("ERROR: Coordinate is already taken. Try again.")
            case _ as Grid:
                return Grid