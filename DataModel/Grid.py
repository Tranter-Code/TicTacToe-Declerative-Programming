from DataModel.Token import *
from DataModel.Coord import *
from typing import Final
import copy

#Let Cell = {X, O, None}
#Let Cell = Token U {None}
#Let Cell = Token option
Cell: TypeAlias = Optional[Token]
Grid : TypeAlias= dict[Coord, Cell]

GRID_DISPLAY: Final[str] = \
"""
  -------------
A | {} | {} | {} |
  |-----------|
B | {} | {} | {} |
  |-----------|
C | {} | {} | {} |
  --A---B---C--
"""

# init_grid : void -> grid
def init_grid() -> Grid:
    return {
        (A(), A()): None,
        (B(), A()): None,
        (C(), A()): None,
        (A(), B()): None,
        (B(), B()): None,
        (C(), B()): None,
        (A(), C()): None,
        (B(), C()): None,
        (C(), C()): None,
    }

def parse_cell_to_string(cell: Cell) -> str:
    match cell:
        case None:
            return " "
        case _ as tkn:
            return str(tkn)

def display_grid(grd: Grid) -> None:
    print(GRID_DISPLAY.format(parse_cell_to_string(grd[(A(), A())]), parse_cell_to_string(grd[(B(), A())]), parse_cell_to_string(grd[(C(), A())]),
               parse_cell_to_string(grd[(A(), B())]), parse_cell_to_string(grd[(B(), B())]), parse_cell_to_string(grd[(C(), B())]),
               parse_cell_to_string(grd[(A(), C())]), parse_cell_to_string(grd[(B(), C())]), parse_cell_to_string(grd[(C(), C())])))


def place_token(tkn: Token, crd: Coord, grd: Grid) -> Optional[Grid]:
    match grd[crd]:
        case None:
            new_grid = copy.deepcopy(grd)
            new_grid |= {crd:tkn}
            return new_grid
        case _:
            return None

def get_random_coord(grd: Grid) -> Coord:
    empty_cells = [Coord for Coord, cell in grd.items() if cell is None]
    return cast(Coord, random.choice(empty_cells))

def check_for_draw(grd: Grid) -> bool:
    empty_cells = [Coord for Coord, cell in grd.items() if cell is None]
    if not empty_cells:
        return True
    return False

def check_for_winner(grd: Grid) -> bool:
    if grd[(A(), A())] == grd[(B(), A())] == grd[(C(), A())] is not None:
        return True
    elif grd[(A(), B())] == grd[(B(), B())] == grd[(C(), B())]is not None:
        return True
    elif grd[(A(), C())] == grd[(B(), C())] == grd[(C(), C())]is not None:
        return True
    elif grd[(A(), A())] == grd[(A(), B())] == grd[(A(), C())]is not None:
        return True
    elif grd[(B(), A())] == grd[(B(), B())] == grd[(B(), C())]is not None:
        return True
    elif grd[(C(), A())] == grd[(C(), B())] == grd[(C(), C())]is not None:
        return True
    elif grd[(A(), A())] == grd[(B(), B())] == grd[(C(), C())]is not None:
        return True
    elif grd[(A(), C())] == grd[(B(), B())] == grd[(C(), A())]is not None:
        return True
    else:
        return False
    
# def check_for_winner(grd: Grid) -> Optional[Token]:
#     match grd:
#         case [(A(), A())] == [(A(), B())] == [(A(), C())]:
#             return grd[(A(), A())]


#          IHG FED CBA
# XMoves = 000 000 111 = 7
# OMoves = 000 000 000
# let Player = Name x Token x PlayerKind x PreviousMoves
 # let PlayerKind = {Human, CPU}
"""
Space vs Time complexity
Space : How much memory / storage do I need to use?
Time  : How long will it take?
"""

"""
X X X
_ _ _
_ _ _

"""