import re
import copy
import sys

print(r'Processing...')
# upper left coord is (0,0)
# goes by (row, col)

'''
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this
'''
# to which direction the flow will exit if coming from x direction
part_types = {
    '|' : {'d': 'u', 'u':'d'},
    'S' : {'d': 'u', 'u':'d'},  # This is cheating
    '-' : {'l': 'r', 'r':'l'},
    'L' : {'u': 'r', 'r':'u'},
    'J' : {'u': 'l', 'l':'u'},
    '7' : {'l': 'd', 'd':'l'},
    'F' : {'d': 'r', 'r':'d'},
}


directions = {
    'u' : (-1,0),
    'd': (1, 0),
    'l': (0, -1),
    'r': (0, 1)
}
opp_dir = {
    'u' : 'd',
    'd': 'u',
    'l': 'r',
    'r': 'l',
}

# I navigate one step through our word, I'm at position (pair of row and col), arriving from dn
# returns next pos and from which dir we arrived
def move(world, pos, dn):
#    print('move', pos, dn, world[pos[0]][pos[1]])
    part = world[pos[0]][pos[1]]                            # The kind of tube I want to go through
    next = part_types[part][dn]                             # The direction the flow leaves the pipe (lrud)
    posdiff = directions[next]                              # The diff in position the move will mean
    nextpos = (pos[0]+posdiff[0], pos[1]+posdiff[1])        # The new position
#    print(next, nextpos, world[nextpos[0]][nextpos[1]])
    return nextpos, opp_dir[next]

# I start at S
def go(world, pos, dn):
    loop = []
    c = 0
    nextpos = pos
    d = dn
    print()
#    print(c, nextpos, d, world[nextpos[0]][nextpos[1]])
    nextpos, d = move(world, nextpos, d)
    loop.append(pos)
    loop.append(nextpos)
#    world[pos[0]][pos[1]] = 'x'
    #    print(c, nextpos, d, world[nextpos[0]][nextpos[1]])
    while nextpos != pos:
        c += 1
#        cpos = nextpos
        nextpos, d = move(world, nextpos, d)
        loop.append(nextpos)
#        world[cpos[0]][cpos[1]] = 'x'
#        print(c, nextpos,d, world[nextpos[0]][nextpos[1]])
    return c / 2, loop

def count_enclosed(world, loop):
    s = 0
    for i in range(len(world)):
        c = 0
        for j in range(len(world[i])):
            if (i,j) in loop:
                if '-' != world[i][j]:
                    c += 1
            else:
                if 1 == c % 2:
                    s += 1
                    print(i,j)
    return s

def findS(world):
    for i in range(len(world)):
        for j in range(len(world[i])):
            if 'S' == world[i][j]:
                return (i,j)
    print('we should never reach this')
    return

def print_world(world):
    for i in world:
        print(i)

#reads the file, returns as list, strips end of line and end of file chars, no other transformation
def readfile(fname):
    s=[]
    with open(fname) as f:
        while True:
            line = f.readline()
            if not line:
                break
            s.append(line.strip())
    return s



def score():
    return 0

def read(fname):
    fc = readfile(fname)
    return fc

