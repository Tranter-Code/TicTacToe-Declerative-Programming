from dataclasses import dataclass
from typing import Optional, TypeAlias, cast
import sys
import random

# X
@dataclass(eq=True, frozen=True)
class X:
    def __str__(self):
        return "X"

# O
@dataclass(eq=True, frozen=True)
class O:
    def __str__(self):
        return "O"

# Let Token = {X} U {O}
Token: TypeAlias = X | O

# parse_token : String -> Token option
def parse_token(s:str)->Optional[Token]:
    # match the String input with each case
    match s:
        # String matched X
        case "X" | "x":
            # Return the X class
            return X()
        # String matches O
        case "O" | "o":
            # Return the O class
            return O()
        # Any other case
        case _ :
            # Return None
            return None
        
#read_token_input : void -> Token
def read_token_input():
    while True:
        result_input = input("Please choose a valid token (X or O): ")
        match parse_token(result_input):
            case None:
                print("ERROR: Token entered is not valid.", file=sys.stderr)
            case _ as tkn:
                return tkn
            
def get_token(tkn_opt: Optional[Token]) -> Token:
    match tkn_opt:
        case X():
            return O()
        case O():
            return X()
        case None:
            return cast(Token, random.choice([X(), O()]))