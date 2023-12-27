import re
from itertools import combinations

import copy
import sys

print(r'Processing...')

def fivetimes(s):
    return (s+'?')*4 + s


def print_world(world):
    for i in world:
        print(i)

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
    ln = re.split(' ', line)
    parts = re.split(',', ln[1])
    return ln[0], [int(x) for x in parts]

# return the list of lengths of #-strings within s
def lenlist(s):
    r = []
    c = 0
    first = True
    for i in s:
        if '.' == i:
            if 0 < c:
                r.append(c)
                c = 0
        else:
            c += 1
    if 0 < c:
        r.append(c)
    return r

def fits(s, pattern):
    p = pattern.replace('.','\.').replace('?','.')
    return re.search(p+'x',s+'x') != None

def full_fits(s, pattern, ll):
    return fits(s,pattern) and lenlist(s) == ll

# s is not longer than pattern
# Returns true if s can be extended that way it is a full fit
def can_be_good(s, pattern, ll):
    if len(s) == len(pattern):
        return full_fits(s, pattern, ll)
    if not fits(s,pattern[:len(s)]):
        return 0
    return can_be_good(s+'.', pattern, ll) or can_be_good(s+'#', pattern, ll)

# returns how many good combinations exist
cnt = 0
xx = 0
def no_good(s, pattern, ll):
#    print('s',s, len(s))
    global cnt
    global xx
    cnt += 1
#    if 1000 == cnt:        sys.exit((0))
    # if length match, return 1 if full fit
    if len(s) == len(pattern):
        if full_fits(s, pattern, ll):
            return 1
        else:
            return 0
    # if is not even a prefix, return 0
    if not fits(s,pattern[:len(s)]):
        return 0
    if s.count('#') + len(pattern) - len(s) < xx - len(ll) + 1:
#        print(s, lls, s.count('#'), len(pattern) - len(s), xx)
        return 0  # we will never have enough #
# if start of list is not good, return 0
    lls = lenlist(s)
    llls = len(lls)
#    print(s, lls)
    if llls > len(ll):
        return 0    # too many groups of #
    if 0 == llls:
        pass
    else:
        for i in range(llls-1):
            if lls[i] != ll[i]:
                return 0
        if lls[llls-1] > ll[llls-1]:                # last group of # is larger than needed
            return 0
#        elif lls[llls-1] == ll[llls-1] and s[-1] == '#':             # last group of # is just good, continue with a .
##            print(s, lls, lls[llls-1])
            return no_good(s+'.', pattern, ll)
        elif s[-1] == '#':                                       # last group of # is small, continue with a #
            return no_good(s+'#', pattern, ll)
    # continue with next letter
    c = pattern[len(s)]
    if '?' != c:
        return no_good(s+c, pattern, ll)
    else:
#        cnt += 1
        return no_good(s+'.', pattern, ll) + no_good(s+'#', pattern, ll)


def read(fname):
    fc = readfile(fname)
    input = []
    for line in fc:
        input.append(readline(line))
    return input

def score(input):
    global xx                               # total count of #
    s = 0
    c = 0
    for i in input:
        xx = 0
        for j in i[1]:
            xx += j
#        print('xx',xx)
#        print(len(i[0]))
        s += no_good('',i[0],i[1])
        c += 1
        print(c, cnt, s)
    return s

#print(no_good('', '???.###????.###????.###????.###????.###', [1,1,3,1,1,3,1,1,3,1,1,3,1,1,3]))
#print(cnt)

input = read(r'C:\py\github\aoc2023\12.dat')
i2 = []
for i in input:
  i2.append((fivetimes(i[0]),i[1]*5))
s = score(i2)
print(s)
assert s == 525152

#input = read(r'C:\py\github\aoc2023\12.dat')
#print(score(input))