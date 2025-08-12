#!/usr/bin/python
from random import shuffle, randrange, sample
from itertools import combinations
from argparse import ArgumentParser

bishop = "♗"
rkr = "♖♔♖"
pieces = "♘♘♕"
pos = [i for i in range(8)]
res = {}

def set_black(black):
    if black:
        global bishop
        global rkr
        global pieces
        bishop = "♟"
        rkr = "♜♚♜"
        pieces = "♞♞♛"

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
        res[pos[ii]] = pieces[ii]

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--black', action='store_true')
    args = parser.parse_args()
    set_black(args.black)
    set_bishops()
    set_rkr()
    set_others()

    final = "".join([res[key] for key in sorted(res.keys())])
    print(final)

