

# Is string s symmetric to position p
# position one is just after first letter
# positions off the boundaries are not axes.
def is_symmetric(s,p):
    if p <= 0 or p >= len(s):
        return False
    l = min(p, len(s) - p)
    for i in range(l):
        if s[p-i-1] != s[p+i]:
            return False
    return True

# return list of possible symmetry axes for a string
def get_axes_s(s):
    if len(s) <= 1:
        return []
    ret = []
    for i in range(1, len(s)):
        if is_symmetric(s,i):
            ret.append(i)
    return ret

# return list of possible symmetry axes for a string, only considering positions in the passed list
def get_axes_sl(s, l):
    if len(s) <= 1:
        return []
    ret = []
    for i in l:
        if is_symmetric(s,i):
            ret.append(i)
    return ret

# return list of possible symmetry axes for a list of strings
# Assumption: each line has equal length
def get_axes_l(l):
    if [] == l:
        return []
    ret = []
    for i in range(1, len(l[0])):          # At first any position is possible
        ret.append(i)
    for i in l:
        ret = get_axes_sl(i,ret)
        if [] == ret:
            return []
    return ret

# return sore of a singel block
def score0(l):
    r = get_axes_l(l)
    if len(r) == 1:
        return r[0]
    #transpose to reuse get_axes_l
    t = [[l[j][i] for j in range(len(l))] for i in range(len(l[0]))]
    r = get_axes_l(t)
    assert len(r) == 1
#    print('')
#    print('t')
#    print(t)
#    print('r',r)
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