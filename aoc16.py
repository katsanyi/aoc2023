#import re
import re
import sys

# upper left coord is (0,0)
# goes by (row, col)

# input: list of tuples (name, focal length), fl=0 means it's a -
# data structure: array of list of tuples: (name, focal length)

#dict: (direction arrived, place -> direction left
stepd = {
    ('r', '.'): 'r',
    ('l', '.'): 'l',
    ('u', '.'): 'u',
    ('d', '.'): 'd',
    ('r', '\\'): 'd',
    ('l', '\\'): 'u',
    ('u', '\\'): 'l',
    ('d', '\\'): 'r',
    ('r', '/'): 'u',
    ('l', '/'): 'd',
    ('u', '/'): 'r',
    ('d', '/'): 'l'
}

def move(d, p, row, col):
    ret = stepd[(d,p)]
    return ret

def print_world(world):
    for i in world:
        print(*i)

def readfile(fname):
    s=[]
    with open(fname) as f:
        while True:
            line = f.readline()
            if not line:
                break
            s.append(line.strip())
    return s

def read(fname):
    fc = readfile(fname)
    return fc


def process(input):
    boxes = [[] for i in range(256)]
    for i in input:
        h = hash(i[0])
        if i[1] > 0:
            found = False
            for j in range(len(boxes[h])):
                if boxes[h][j][0] == i[0]:
                    boxes[h][j] = (i[0], i[1])
                    found = True
            if not found:
                boxes[h].append(i)
        else:
            for j in boxes[h]:
                if j[0] == i[0]:
                    boxes[h].remove(j)
    return boxes

# returns the fp of a single box
# input is the box itself and its seq number
def focus_power(b, bno):
    s = 0
    for i in range(len(b)):
        s += (bno + 1) * (i + 1) * b[i][1]
    return s

def score(boxes):
    s = 0
    for i in range(len(boxes)):
        s += focus_power(boxes[i],i)
    return s