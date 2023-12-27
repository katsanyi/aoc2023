import re
import copy
import sys

print(r'Processing...')
# upper left coord is (0,0)
# goes by (row, col)

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

def is_empty_row(world,row):
    for i in world[row]:
        if '#' == i:
            return False
    return True

def is_empty_col(world,col):
    for i in range(len(world)):
        if '#' == world[i][col]:
            return False
    return True


# returns a list of coordinates, considering expansion as well
## assumption: each line is of same length
def get_coords(world,ratio):
    pw = []
    ii = 0
    for i in range(len(world)):
        jj = 0
        if is_empty_row(world,i):
            ii += 1
            ii += ratio - 1
            continue
        for j in range(len(world[i])):
            if is_empty_col(world,j):
                jj += ratio - 1
            if '#' == world[i][j]:
                pw.append((ii,jj))
            jj += 1
        ii += 1
    return pw

def get_dist(g1,g2):
    return abs(g1[0]-g2[0]) + abs(g1[1] - g2[1])

# sum of the shortest path between all pairs of galaxies
def score(pworld):
    s = 0
    for i in range(len(pworld)):
        for j in range(0, len(pworld)):
            d = get_dist(pworld[i],pworld[j])
            s += d
    return s / 2
