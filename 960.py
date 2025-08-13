#!/usr/bin/python
from random import shuffle, randrange, sample
from itertools import combinations
from argparse import ArgumentParser

bishop = "♗"
knight = "♘"
queen = "♕"
king = "♔"
rook = "♖"
pawn = "♙"

pos = [i for i in range(8)]
res = {}

def set_black(black):
    if black:
        global bishop, knight, rook, queen, king, pawn
        global rkr
        global others
        bishop = "♟"
        knight = "♞"
        queen = "♛"
        king =  "♚"
        rook = "♜"
        pawn = "♟"


    rkr = rook + king + rook
    others = knight + knight + queen

def set_bishops():
    """Bishops must go on opposite colors."""
    bis1 = randrange(4) * 2
    res[bis1] = bishop
    pos.remove(bis1)
    bis2 = randrange(4) * 2 + 1
    res[bis2] = bishop
    pos.remove(bis2)

def set_rkr():
    """King must go between the rooks"""
    trips = [combo for combo in combinations(pos, 3)]
    trip = sample(trips, 1)[0]
    for ii in range(len(trip)): # which will be 3 ;-)
        res[pos[ii]] = rkr[ii]
        pos.remove(pos[ii])
    #print(res)

def set_others():
    shuffle(pos)
    for ii in range(len(pos)):
        res[pos[ii]] = others[ii]

def show_pieces(pieces):
    pieces = pieces.lower()
    out = ""
    for char in pieces:
        if char == 'k':
            out += king
        if char == 'n':
            out += knight
        if char == 'r':
            out += rook
        if char == 'q':
            out += queen
        if char == 'b':
            out += bishop
        if char == 'p':
            out += pawn
    print(out)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--black', action='store_true')
    parser.add_argument('--pieces', help="show specific pieces")
    args = parser.parse_args()
    set_black(args.black)
    if args.pieces:
        show_pieces(args.pieces)
    else:
        set_bishops()
        set_rkr()
        set_others()

    final = "".join([res[key] for key in sorted(res.keys())])
    print(final)

