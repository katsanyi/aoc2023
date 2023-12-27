import re

print(r'Processing...')

digits = '0123456789'
digitsperiod = '0123456789.'
numbers = []
symbols = []

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

winners = []
have = []
wincount = []
counts = []

#todo: adds an empty to have
def processpart(part):
    partdict = {}
    numbers = re.split(' ',part)
    for i in numbers:
        if i != '': #ugly hack
          partdict[i] = True
    return partdict

def processline(line):
    parts = re.split(': | \| ', line)
    winners.append((processpart(parts[1])))
    have.append((processpart(parts[2])))


def process(fname):
    fc = readfile(fname)
    for line in fc:
        processline(line)

    for i in range(len(winners)):
        c = 0
        for j in have[i]:
            if j in winners[i]:
                c += 1
        wincount.append(c)

def score1():
    s=0
    for c in wincount:
        if c == 0:
            score = 0
        else:
            score = pow(2,c-1)
        s += score
    return s

def score2():
    for i in range(len(winners)):
        counts.append(1)
    for i in range(len(winners)):
        for j in range(i+1,i+1+wincount[i]):
#            print(i,j,wincount[i], counts)
            counts[j] += counts[i]
    s=0
    for i in counts:
        s += i
    return s


def process2(fname):
    r = 0
    s = 0
    fc = readfile(fname)
    for line in fc:
        processline(line)
    for i in range(len(winners)):
        c = 0
        for j in have[i]:
            if j in winners[i]:
                c += 1
    return s

def test_find_numbers():
    pass


test_find_numbers()

process(r'C:\py\github\aoc2023\4.dat')
s = score1()
#myassert(26346, s)
s = score2()
print(s)