from dataclasses import dataclass
from typing import Optional, TypeAlias, Tuple
import sys

# Coord
# A
@dataclass(eq=True, frozen=True)
class A:
    pass
# B
@dataclass(eq=True, frozen=True)
class B:
    pass
# C
@dataclass(eq=True, frozen=True)
class C:
    pass

# Let CoordAxis = {A, B, C}
CoordAxis: TypeAlias  = A | B | C
# let Coord = CoordAxis X CoordAxis
# This is a Tuple literal
# Values vs Types syntax
# Discuss type vs value level syntax 
Coord: TypeAlias = Tuple[CoordAxis, CoordAxis]

def parse_coord(s:str)->Optional[Coord]:
    match s:       
        case "A.A" | "A.a" | "a.A" | "a.a":
            return (A(), A())
        case "A.B" | "A.b" | "a.B" | "a.b":
            return (A(), B())
        case "A.C" | "A.c" | "a.C" | "a.c":
            return (A(), C())
        case "B.A" | "B.a" | "b.A" | "b.a":
            return (B(), A())
        case "B.B" | "B.b" | "b.B" | "b.b":
            return (B(), B())
        case "B.C" | "B.c" | "b.C" | "b.c":
            return (B(), C())
        case "C.A" | "C.a" | "c.A" | "c.a":
            return (C(), A())
        case "C.B" | "C.b" | "c.B" | "c.b":
            return (C(), B())
        case "C.C" | "C.c" | "c.C" | "c.c":
            return (C(), C())
        case _:
            return None

# read_coord_input: void -> Coord
# Use inferred type at the moment annotations can be added later to enforce that the inferred type is maintained
def read_coord_input():
    while True:
        result_input = input("Please input a valid coordinate: ")
        match parse_coord(result_input):
            case None:
                print("ERROR: Please enter a valid coordinate.", file=sys.stderr)
            case _ as coordinate:
                return coordinate