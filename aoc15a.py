#import re
import sys

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
    ret = fc[0].split(',')
    return ret

def score1(s):
    ret = 0
    for i in s:
        a = ord(i)
        ret += a
        ret *= 17
        ret = ret % 256
    return ret

def score(l):
    s = 0
    for i in l:
        s += score1(i)
    return s