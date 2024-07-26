import sys
from enum import Enum
from typing import TypeAlias, Final, Optional
from dataclasses import dataclass

MAIN_MENU_MESSAGE: Final[str] = \
"""
Welcome to Tic-Tac-Toe.
What would you like to do?
1. Start a single player game.
2. Start a 2-player game
3. Exit game
"""

class MenuOption(Enum):
    StartSinglePlayer = "1"
    StartTwoPlayer = "2"
    ExitGame = "3"

def display_main_menu() -> None:
    print(MAIN_MENU_MESSAGE, file=sys.stdout)
  
# parse_menu_choice : str -> Option<Menu>
def parse_menu_choice(s:str) -> Optional[MenuOption]:
    match s:
        case "1":
            return MenuOption.StartSinglePlayer
        case "2":
            return MenuOption.StartTwoPlayer
        case "3":
            return MenuOption.ExitGame
        case _  :
            return None
    
# read_menu_choice : void -> Menu
def read_menu_choice() -> MenuOption:
    while True:
        choice = input("Input Menu Option (e.g. 2): ")
        match parse_menu_choice(choice):
            case MenuOption.StartSinglePlayer | MenuOption.StartTwoPlayer | MenuOption.ExitGame as x:
                return x
            case None: 
                # print out error message 
                # iterate or recurse
                print("ERROR: Invalid menu option must be one of the valid options displayed (e.g. 1)", file=sys.stderr)

