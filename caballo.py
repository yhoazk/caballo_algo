#!/usr/bin/python
import random
import copy
DIMENSION = 8
SEED = 5
Delta = [[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1],[-2,1]]

def myDeepCopy(a):
    if (isinstance(a, list) or isinstance(a, tuple)):
        return [myDeepCopy(element) for element in a]
    else:
        return copy.copy(a)

# create a DIMENSION x DIMENSION array, whit all empty elements
check_board_SW = [["E"]*DIMENSION]*DIMENSION #create copies of the same row
check_board = myDeepCopy(check_board_SW)
initial_pos_afil = [3,5]






def point(x,y):
    print "drawPoint(",
    print x,
    print ",",
    print y,
    print ",'X'",
    print ");"

def line(a,b):
    print "drawMov(",
    print a[0],
    print ",",
    print a[1],
    print ",",
    print b[0],
    print ",",
    print b[1],
    print ");"

"""
Whit this function the white(W), black(B), and Empty(E) (U used) elements
are asigned in every square of the checkboard
The input paramaters are,
    W: number of white pieces
    B: number of black pieces
"""
def generate_chess(W, B):
    global check_board
    global DIMENSION
    global SEED
    element = set(range(1,DIMENSION * DIMENSION))
    random.seed(SEED)
    white_piece_pos = 0
    black_piece_pos = 0
    for a in range(W):
        white_piece_pos = random.choice(list(element))
        element.remove(white_piece_pos) # This way the element is not picket twice
        check_board[white_piece_pos%DIMENSION][white_piece_pos/DIMENSION] = "W"
        point(white_piece_pos%DIMENSION, white_piece_pos/DIMENSION)

    for k in range(B):
        black_piece_pos = random.choice(list(element))
        element.remove(black_piece_pos) # This way the element is not picket twice
        check_board[black_piece_pos%DIMENSION][black_piece_pos/DIMENSION] = "B"
        point(black_piece_pos%DIMENSION, black_piece_pos/DIMENSION)

def get_next_list(knigth_pos):
    next_pos_sw = [[0]*2]*8 #array to store the next possible positions
    next_pos = myDeepCopy(next_pos_sw)
    global DIMENSION
    for i in range(DIMENSION):
        next_pos[i][0] = knigth_pos[0] + Delta[i][0]
        next_pos[i][1] = knigth_pos[1] + Delta[i][1]
    return next_pos
"""

"""
def next_list(initial):
    next_posible = get_next_list(initial)
    # Create a 8x2 array
    next_val = [["s" for i in range(2)] for j in range(len(next_posible))]
    #print next_val
    empty_cntr = 0
    for index in range(len(next_posible)):
        if "E" == check_board[next_posible[index][0]][next_posible[index][1]]:
            next_val[empty_cntr][0] = next_posible[index][0]
            next_val[empty_cntr][1] = next_posible[index][1]
            empty_cntr +=  1
            #print "//found"
        #elif "W" == check_board[next_posible[index][0]][next_posible[index][1]]:
            #print "//white"
    return next_val
"""
Gets as a parameter the initial position, and a set of numbers which represent the elements
from which to pick the next element, the element represent the next possible possitions
that the piece may take
"""
def solver(x0, postion_set):
    global check_board
    # get the list of the new possible positions based on the current
    next_xy = next_list(x0)

    print next_xy
    elements_set = set(range(8))
    # pick a possible path
    picked_path = random.choice(list(elements_set))
    if  next_xy[picked_path][0] == 's' or  next_xy[picked_path][1] == 's':
        #this element isn't valid, use another and delete this one
        #check if there are available elements in the set
        if len(elements_set) > 0:
            picked_path = random.choice(list(elements_set))
        else:
            #there are no more elements to pick, check if the problem is solved, if not return the next cycle

    print "Picj: x=",
    print next_xy[picked_path][0],
    print next_xy[picked_path][1],
    #elements_set.remove(picked_path)



def main():
    generate_chess(8,8)
    tst =  solver(initial_pos_afil)
    print "////////////__"
    print tst
#    mySet = set(tst)
#    print mySet
#    k = random.choice(list(tst))
#    mySet.remove(k)
#    print k
#    print mySet
#    if 's' in k:
#        print "no"
#    else:
#        print "ies"
    for x in range(8):
        print "drawPoint_small(",
        print initial_pos_afil[0] + Delta[x][0] ,
        print ",",
        print initial_pos_afil[1] + Delta[x][1],
        print ",'G'",
        print ");"


if __name__ == "__main__":
    main()
