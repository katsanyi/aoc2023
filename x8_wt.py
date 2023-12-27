import re
import copy
import sys

print(r'Processing...')
direction_list = ''
#dict. key: start, value: pair of dest
next_place = {}

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

def myassert(a,b):
    if a != b:
        print('Assertion failed', a, ' != ',b)


def readline(line):
    s = re.sub(' |\(|\)','',line)
    parts = re.split('=|,', s)
    return (parts[0],(parts[1],parts[2]))

def processline(line):
    return line

def read(fname):
    next_place = {}
    fc = readfile(fname)
    direction_list = fc[0]
    fc.pop(0)
    fc.pop(0)
    for i in fc:
        h = processline(readline(i))
        next_place[h[0]] = h[1]
    return direction_list, next_place

def get_dir(i,direction_list):
    return direction_list[i % len(direction_list)]


def score(direction_list,next_place):
    i=0
    p = 'AAA'
    while 'ZZZ' != p:
        d = get_dir(i,direction_list)
        if 'L' == d:
            di = 0
        else:
            di = 1
        p = next_place[p][di]
#        print(i,d,p)
        i += 1
    return i


def start_place(next_place):
    p = []
    for i in next_place:
        if 'A' == i[2]:
            p.append(i)
    return p



def is_end_place(p):
    for i in p:
        if 'Z' != i[2]:
            return False
    return True


def score2(direction_list,next_place):
    c=0
    p = start_place(next_place)
    q = []
    print()
    while not is_end_place(p):
        d = get_dir(c, direction_list)
        if 'L' == d:
            di = 0
        else:
            di = 1
        for i in range(len(p)):
            p[i] = next_place[p[i]][di]
            if 'Z' == p[i][2]:
                print('Reached end in one thread:',c,i,p[i])
                q.append((c,i,p[i]))
        c += 1
        if 0 == c % 100000:
            break
    print('Here are the data to determine cycles:')
    for i in range(len(p)):
        for j in q:
            if j[1] == i:
                print(j)
    return c


'''
direction_list, next_place = read(r'C:\py\github\aoc2023\8.dat')
s = score(direction_list, next_place)
print(s)
myassert(17873,s)
#sys.exit((0))

#print(17873*19631*17287*12599*21389*20803-1)
#This is too high
'''
'''
get the length of cycles:
17873 19631 17287 12599 21389 20803
product would be too high: 34002592904266863793513273
get least common multiple (https://www.calculatorsoup.com/calculators/math/lcm.php)
15746133679061
'''

#s = score2()
#print('finally:',s)
#myassert(17873,s)

#read(r'C:\py\github\aoc2023\8.dat')
#print(score())
