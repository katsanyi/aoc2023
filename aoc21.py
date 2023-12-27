import re
import copy


def readfile(fname):
    s=[]
    with open(fname) as f:
        while True:
            line = f.readline()
            if not line:
                break
            s.append(line.strip())
    return s

def readline(s : str):
    r = []
    p = s.find('S')
    for i in s:
        r.append('.' if i == 'S' else i )
    return r, p

def read(sl):
    pos = (0,0)
    row = -1
    ret = []
    for i in sl:
        row += 1
        (l,p) = readline(i)
        ret.append(l)
        if p != -1:
            pos = (row, p)
    return (ret, pos)

def step(map, current):
    next = []
    for i in current:
        for j in [(0,1),(0,-1),(1,0),(-1,0)]:
            row = i[0] + j[0]
            col = i[1] + j[1]
            pos = (row, col)
            if row < 0 or row >= len(map) or col < 0 or col > len(map[0]):
                pass
            elif map[row][col] == '#':
                pass
            elif pos in next:
                pass
            else:
                next.append(pos)
    return next

def nstep(input, stepsno):
    map = input[0]
    current = [input[1]]
    for i in range(stepsno):
        next = step(map, current)
        current = next
        print(len(next))
    return len(current)