import re
import copy
import sys

print(r'Processing...')

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


def readline(line):
    parts = re.split(' ', line)
    return [int(x) for x in parts]

def getdiff(l):
    prev = None
    next = []
    for i in l:
        if None != prev:
            next.append(i - prev)
        prev = i
    return next

def is_all_null(s):
    for i in s:
        if 0 != i:
          return False
    return True

def processline(line):
    i = line
    r = [line]
    while not is_all_null(i):
        i = getdiff(i)
        r.append(i)
    return r

def set_next(ll):
    if len(ll) <= 1:
        return
    for i in range(len(ll)-2,-1,-1):
        ll[i].append(ll[i][-1] + ll[i+1][-1])
    return

def set_prev(ll):
    if len(ll) <= 1:
        return
    for i in range(len(ll)-2,-1,-1):
        ll[i].insert(0,ll[i][0] - ll[i+1][0])
    return


def score(ll):
    l = 0
    r = 0
    for i in ll:
#        print('im1',i[0][-1])
        l += i[0][0]
        r += i[0][-1]
    return l,r

def read(fname):
    fc = readfile(fname)
    ll = []
    for i in fc:
        l = processline(readline(i))
        set_next(l)
        set_prev(l)
        ll.append((l))
    return score(ll)

