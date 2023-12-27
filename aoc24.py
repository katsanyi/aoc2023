import re
import sys


def sign(a):
    if a == 0:
        return 0
    elif a > 0:
        return 1
    else:
        return -1

def readfile(fname):
    s=[]
    with open(fname) as f:
        while True:
            line = f.readline()
            if not line:
                break
            s.append(line.strip())
    return s

def readline(s):
    l = re.split(', | @ ',s)
    ret = ((int(l[0]),int(l[1]),int(l[2])),(int(l[3]),int(l[4]),int(l[5])))
    return ret

def read(slist):
    ret = []
    for i in slist:
        j = readline(i)
        ret.append(j)
    return ret

def value_at(e, x):
    x0 = e[0][0]
    y0 = e[0][1]
    dx = e[1][0]
    dy = e[1][1]
    y = dy / dx * (x - x0) + y0
    return y

def intersection_point0(e1, e2):
    if e1[1][0] * e2[1][1] == e2[1][0] * e1[1][1]:
        return (0,0)
    b1 = value_at(e1,0)
    a1 = value_at(e1,1) - b1
    b2 = value_at(e2,0)
    a2 = value_at(e2,1) - b2
    if a1 == a2:
        print(e1, '-----', e2,'a1', a1, 'a2', a2)
        return (0,0)                    # dirty hack, (0,0) is outside of test area
    x = (b2 - b1) / (a1 - a2)
    y = value_at(e1, x)
    return (x,y)

def is_intersecting00(e1, e2, mn, mx):
    p = intersection_point(e1, e2)
    if mn <= p[0] <= mx and mn <= p[1] <= mx:
        if sign(p[0] - e1[0][0]) == sign(e1[1][0])  and sign(p[0] - e2[0][0]) == sign(e2[1][0]):
            return True
    return  False

def is_intersecting0(e1, e2, mn, mx):
    y11 = value_at(e1, mn)      # e1 at min
    y12 = value_at(e1, mx)      # e1 at max
    y21 = value_at(e2, mn)
    y22 = value_at(e2, mx)
    if y11 < y21 and  y12 > y22:
#        print('1', y11, y12, y21, y22)
        return True
    elif y11 > y21 and  y12 < y22:
#        print('2', y11, y12, y21, y22)
        return True
    else:
        return False


def is_intersecting(e1, e2, mn, mx):
    if e1[1][0] * e2[1][1] == e2[1][0] * e1[1][1]:
        return False    # could be identical as well
    y11 = value_at(e1, mn)
    y12 = value_at(e1, mx)
    y21 = value_at(e2, mn)
    y22 = value_at(e2, mx)

    dy1 = y21 - y11     # diff at mn
    dy2 = y22 - y12     # diff at mx
    if sign(dy1) == sign (dy2):
        return False
    dy1 = y21 - y11
    dy2 = y22 - y12
    dx1 = abs(dy1) * (mx - mn) / (abs(dy1) + abs(dy2))
    x = dx1 + mn
    print('e1',e1)
    print('e2',e2)
    print('dx1',dx1)
    print('x',x)
    if sign(x - e1[0][0]) != sign(e1[1][0]):
        print('past for e1')
        return False
    if sign(x - e2[0][0]) != sign(e2[1][0]):
        print('past for e2')
        return False
    return True


def score(l, mn, mx):
    s = 0
    ll = len(l)
    for i in range(ll):
        for j in range(i+1, ll):
            print(i,j)
            if is_intersecting(l[i], l[j], mn, mx):
                s += 1
            if j == 10:
                sys.exit(0)
    return s