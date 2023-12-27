#import re
import sys

def print_world(world):
    for i in world:
        print(*i)

def print_dworld(world):
    for i in range(10):
        print()
        for j in range(10):
          print(world[i],[j], end='')


def readfile(fname):
    s=[]
    with open(fname) as f:
        while True:
            line = f.readline()
            if not line:
                break
            s.append(line.strip())
    return s

#Assumption: all lines are of equal length
def read(fname):
    fc = readfile(fname)
    width = len(fc[0])
    depth = len(fc)
    ret = [[0] * width for i in range(depth)]
    for i in range(width):
        for j in range(depth):
            if fc[j][i] == '.':
                ret[j][i] = 0
            elif fc[j][i] == 'O':
                ret[j][i] = 1
            else:
                ret[j][i] = 9
    return ret

def move(ret,d1,d2):
    width = len(ret[0])
    depth = len(ret)

    changed = True
    while changed:
        changed = False
        for i in range(width): #!!!!!
            for j in range(depth):
                if j + d1 < 0 or j + d1 >= depth or i + d2 < 0 or i + d2 >= width:
#                    print('skipped:', i, j, d1, d2, width, depth, j + d1, i + d2)
                    continue
#                print('ij',i,j, d1, d2, width, depth, j + d1, i + d2)
                if ret[j][i] == 1 and ret[j + d1][i + d2] == 0:
                    ret[j + d1][i + d2] = 1
                    ret[j][i] = 0
                    changed = True
    #    print_world(ret)
    return ret


def process(ret):
    move(ret,-1,0)
    return ret

def process1(ret):
    move(ret, -1,  0)    # north
#    print('north done')
#    print(ret)
    move(ret,  0, -1)    # west
#    print('west done')
#    print(ret)
    move(ret,  1,  0)    # south
#    print('south done')
#    print(ret)
    move(ret,  0,  1)    # east
#    print('east done')
#    print(ret)
    return ret


def process0(ret):
    width = len(ret[0])
    depth = len(ret)
    #ret = [[0] * width for i in range(depth)]

    changed = True
    while changed:
        changed = False
        for i in range(width):
            for j in range(1,depth):
                if ret[j][i] == 1 and ret[j - 1][i] == 0:
                    ret[j - 1][i] = 1
                    ret[j][i] = 0
                    changed = True
#    print_world(ret)
    return ret

def score(ret):
    s = 0
    width = len(ret[0])
    depth = len(ret)
    for i in range(width):
        for j in range(0, depth):
            if ret[j][i] == 1:
                score = depth - j
                s += score
#    print('s',s)
    return s

def score2(ret):
    for i in range(100):
#        print('i-----',i)
        process1(ret)
        sc = score(ret)
        print(i, sc)


input = read(r'C:\py\github\aoc2023\14_.dat')
ret = process1(input)
score2(ret)
# answer is 102509
# 9 different ones are cycling after a period
