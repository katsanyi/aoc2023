import re
import copy
import sys

print(r'Processing...')
time = []
dist = []

def readfile(fname):
    s=[]
    with open(fname) as f:
        while True:
            line = f.readline()
            if not line:
                break
            s.append(line.strip())
    return s

def myassert(a,b):
    if a != b:
        print('Assertion failed', a, ' != ',b)


def processline(line):
    parts = re.split(' +', line)
    parts.pop(0)
    return [int(x) for x in parts]

def test_processline():
    myassert([7,15,30],processline('Time:      7  15   30'))
    myassert([9,40,200],processline('Distance:  9  40  200'))

test_processline()

#assumption: file is not empty
def read(fname):
    fc = readfile(fname)
    global time
    global dist
    time = processline(fc[0])
    dist = processline(fc[1])
#    time.extend(processline(fc[0]))
#    dist.extend(processline(fc[1]))

def test_read():
    read(r'C:\py\github\aoc2023\6_.dat')
    myassert([7,15,30], time)
    myassert([9,40,200], dist)

test_read()

# how many ways we can beat d dist in t time
def waysno(t, d):
    s = 0
    for i in range(t+1):
        dd = (t-i)*i
        if dd > d:
          s += 1
    return s

def test_waysno():
    myassert(4,waysno(7,9))
    myassert(8,waysno(15,40))
    myassert(9,waysno(30,200))

test_waysno()

def score():
    p = 1
    for i in range(len(time)):
        wn = waysno(time[i],dist[i])
        #print(wn)
        if i % 1000 == 0:
            print(i)
        p *= wn
    return p

read(r'C:\py\github\aoc2023\6_.dat')
print(score())

read(r'C:\py\github\aoc2023\6.dat')
print(score())

read(r'C:\py\github\aoc2023\6_b.dat')
print(score())

read(r'C:\py\github\aoc2023\6b.dat')
print(score())
