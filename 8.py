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

def test_readline():
    myassert(('AAA',('BBB','CCC')),readline('AAA = (BBB, CCC)'))


test_readline()
#sys.exit(0)

def processline(line):
    return line

def test_processline():
    pass

test_processline()

def read(fname):
    global direction_list
    global next_place
    map = {}
    fc = readfile(fname)
    dir = fc[0]
    fc.pop(0)
    fc.pop(0)
    for i in fc:
        h = processline(readline(i))
        map[h[0]] = h[1]

def test_read():
    read(r'C:\py\github\aoc2023\8_.dat')
    myassert('LLR', direction_list)
    myassert({'AAA': ('BBB', 'BBB'), 'BBB': ('AAA', 'ZZZ'), 'ZZZ': ('ZZZ', 'ZZZ')}, next_place)

test_read()
test_read()
#sys.exit(0)

def get_dir(i):
    return direction_list[i % len(direction_list)]

def test_dir():
    read(r'C:\py\github\aoc2023\8_.dat')
    myassert('L',get_dir(0))
    myassert('L',get_dir(1))
    myassert('R',get_dir(2))
    myassert('L',get_dir(3))

test_dir()
#sys.exit(0)

def score():
    i=0
    p = 'AAA'
    while 'ZZZ' != p:
        d = get_dir(i)
        if 'L' == d:
            di = 0
        else:
            di = 1
        p = next_place[p][di]
#        print(i,d,p)
        i += 1
    return i

def test_score():
  read(r'C:\py\github\aoc2023\8_.dat')
  print(score())
  myassert(6,score())

test_score()
#sys.exit(0)

def start_place():
    p = []
    for i in next_place:
        if 'A' == i[2]:
            p.append(i)
    return p

def test_start_place():
    read(r'C:\py\github\aoc2023\8_2.dat')
    myassert(['11A', '22A'],start_place())

test_start_place()

def is_end_place(p):
    for i in p:
        if 'Z' != i[2]:
            return False
    return True

def test_is_end_place():
    myassert(True,is_end_place([]))
    myassert(True,is_end_place(['AAZ']))
    myassert(True,is_end_place(['AAZ','BBZ']))
    myassert(False,is_end_place(['AAZ','BBZ','BBB']))
    myassert(False,is_end_place(['BBB']))

test_is_end_place()

#sys.exit(0)

def score2():
    c=0
    p = start_place()
#    print(p)
    q = []
    while not is_end_place(p):
        d = get_dir(c)
        if 'L' == d:
            di = 0
        else:
            di = 1
        for i in range(len(p)):
            p[i] = next_place[p[i]][di]
            if 'Z' == p[i][2]:
                print(c,i,p[i])
                q.append((c,i,p[i]))
        c += 1
#        print(c,p,d)
#        if 10000 == c:
#            break
        if 0 == c % 100000:
            break
        if 0 == c % 10000000:
            print(c)
    for i in range(len(p)):
        for j in q:
            if j[1] == i:
                print(j)
    return c

def test_score2():
  read(r'C:\py\github\aoc2023\8_2.dat')
  print(score2())
  myassert(6,score2())

#test_score2()

read(r'C:\py\github\aoc2023\8.dat')
#s = score()
#print(s)
#myassert(17873,s)

print(17873*19631*17287*12599*21389*20803-1)
#This is too high
'''
get the length of cycles:
17873 19631 17287 12599 21389 20803
product would be too high: 34002592904266863793513273
get least comon multiple (https://www.calculatorsoup.com/calculators/math/lcm.php)
15746133679061
'''

s = score2()
print('finally:',s)
#myassert(17873,s)

#read(r'C:\py\github\aoc2023\8.dat')
#print(score())
