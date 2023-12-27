import numpy as np

directions = {
    'U' : (-1,0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

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
    l = s.split(' ')
    ret = (l[0],int(l[1]))
    return ret

dircode = {
    '0': 'R',
    '1': 'D',
    '2': 'L',
    '3': 'U'
}

def readline2(s : str):
    '''

    :param s: string, for example
    :return: a tuple, for example ('R', 461937)
    '''

    l = s.split(' ')
    d = dircode[l[2][7]]
    steps = int(l[2][2:7], base=16)
    ret = (d, steps)
    return ret


def read(slist):
    ret = []
    for i in slist:
        ret.append(readline(i))
    return ret

def read2(slist):
    ret = []
    for i in slist:
        ret.append(readline2(i))
    return ret

def process(tlist):
    ret = {}
    ret[(0,0)] = '#'
    row = 0
    col = 0
    for i in tlist:
        if i[0] in 'LR':
            c = '-'
        elif i[0] == 'U':
            c = '^'
        else:
            c = 'ˇ'
        if i[0] in 'UD':
            ret[(row,col)] = c
        for j in range(i[1]):
            delta = directions[i[0]]
            row += delta[0]
            col += delta[1]
#            ret.add((row,col))
            ret[(row,col)] = c
    return ret

def process3(tlist):
    '''
    Gets the tuple list of moves
    returns the vertices of the poligon defined
    '''
    ret = [(0,0)]
    row = 0
    col = 0
    perim = 0
    for i in tlist:
        delta = directions[i[0]]
        length = i[1]
        perim += length
        row += delta[0] * length
        col += delta[1] * length
        pos = (row,col)
        if pos != (0,0):
            ret.append(pos)
        else:
            pass
            print('Returned to 00')
    return (ret, perim)

def process2(pset):
    s = 0
#    print()
    minrow = min([x[0] for x in pset])
    mincol = min([x[1] for x in pset])
    maxrow = max([x[0] for x in pset])
    maxcol = max([x[1] for x in pset])
    lastud = 'x'
    for i in range(minrow, maxrow + 1):
        is_in = False
#        print()
        for j in range(mincol, maxcol + 1):
            if (i,j) in pset:
                c = pset[(i,j)]
                if c in '^ˇ' and lastud != c:
                    is_in = not is_in
                    lastud = c
#                print(c, end='')
                s += 1
            else:
                if is_in:
#                    print('o', end='')
                    s += 1
#                else:
#                    print('.', end='')
    return s

def shoelace(vlist : list):
    '''

    :param vlist: list of vertices (tuples of (row, col)
    :return: area of poligon
    '''
# x,y are arrays containing coordinates of the polygon vertices
    xl = []
    yl =  []
    for i in vlist:
        xl.append(i[0])
        yl.append(i[1])
    x=np.array(xl)
    y=np.array(yl)
    i=np.arange(len(x))
    Area=np.abs(np.sum(x[i-1]*y[i]-x[i]*y[i-1])*0.5) # one line of code for the shoelace formula
    return Area

def shoelace2(vlist : list):
    total=0
    i = 0
    while i != len(vlist)-1:
      total+=vlist[i][0]*vlist[i+1][1]
      total-=vlist[i+1][0]*vlist[i][1]
      i+=1
    return abs(total +vlist[-1][0]*vlist[0][1] -vlist[-1][-1]*vlist[0][0])/2