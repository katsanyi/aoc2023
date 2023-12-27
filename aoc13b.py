import sys

def print_world(world):
    for i in world:
        print(*i)

# we are looking for 'mirror' axes, that is, axes with exactly n errors in mirror image
# assumption: same length
def diff(s1, s2):
    s = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            s += 1
    return s

# Is string s symmetric to position p
# position one is just after first letter
# positions off the boundaries are not axes.
def is_symmetric(s,p):
    if p <= 0 or p >= len(s):
        return 99
    l = min(p, len(s) - p)
    cdiff = 0
    for i in range(l):
        cdiff += diff(s[p-i-1], s[p+i])
    return cdiff

# return list of possible symmetry axes for a string
# for each axe it returns how many mismatches
def get_axes_s(s):
    if len(s) <= 1:
        return []
    ret = []
    for i in range(1, len(s)):
        c = is_symmetric(s,i)
        ret.append([i,c])
    return ret


# return list of possible symmetry axes for a list of strings
# Assumption: each line has equal length
def get_axes_l(l):
#    print('l',l)
    if [] == l:
        return []
    ret = []
    for i in l:
#        print('i',i)
        axs = get_axes_s(i)
        if [] == ret:
            ret = axs
        else:
            for j in range(len(ret)):
                ret[j][1] += axs[j][1]
#        print('axs',axs)
#        print('ret',ret)
    r2 = []
    for i in ret:
        if i[1] == 1:
            r2.append(i[0])
    assert len(r2) < 2
    return r2

# return sore of a singel block
def score0(l):
    print('l')
    print_world(l)
    r = get_axes_l(l)
    print('r',r)
    if len(r) == 1:
        return r[0]
    #transpose to reuse get_axes_l
    t = [[l[j][i] for j in range(len(l))] for i in range(len(l[0]))]
    r = get_axes_l(t)
    print('r2',r)
    #assert len(r) == 1
    return 100*(r[0])

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
    l = []
    ret = []
    for i in fc:
        if '' != i:
            l.append(i)
        else:
            ret.append(l)
            l = []
    ret.append(l)
    return ret


def score(input):
    s = 0
    for i in input:
        s += score0(i)
    return s

get_axes_l([
'#.##..##.',
'..#.##.#.',
'##......#',
'##......#',
'..#.##.#.',
'..##..##.',
'#.#.##.#.',
])

'''
input = read(r'C:\py\github\aoc2023\13_.dat.txt')
s = score(input)
print(s)
'''