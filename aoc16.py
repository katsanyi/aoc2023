from dataclasses import dataclass

@dataclass(unsafe_hash=True)
class Position:
    row: int
    col: int
    directions = {
        'u': (-1, 0),
        'd': (1, 0),
        'l': (0, -1),
        'r': (0, 1)
    }
    def step(self, direction):
        self.row += self.directions[direction][0]
        self.col += self.directions[direction][1]

# upper left coord is (0,0)
# goes by (row, col)


#dict: (direction arrived, place) -> direction left
stepd = {
    ('r', '|'):  ['u','d'],
    ('l', '|'):  ['u','d'],
    ('u', '|'):  ['u'],
    ('d', '|'):  ['d'],
    ('r', '-'):  ['r'],
    ('l', '-'):  ['l'],
    ('u', '-'):  ['l', 'r'],
    ('d', '-'):  ['l', 'r'],
    ('r', '.'):  ['r'],
    ('l', '.'):  ['l'],
    ('u', '.'):  ['u'],
    ('d', '.'):  ['d'],
    ('r', '\\'): ['d'],
    ('l', '\\'): ['u'],
    ('u', '\\'): ['l'],
    ('d', '\\'): ['r'],
    ('r', '/'):  ['u'],
    ('l', '/'):  ['d'],
    ('u', '/'):  ['r'],
    ('d', '/'):  ['l']
}

def move(d, p):
    '''

    :param d: arriving direction
    :param p: symbol at positon
    :return: list of outgoing directions (1 or 2 directions)
    '''
    ret = stepd[(d,p)]
    return ret

def xprint_world(world):
    for i in world:
        print(*i)

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
    return fc

def process0(slist: list[str], start):
    energized = set()
    visited = set()
    current = [start]
#    zz = Position(0,0)
#    current = [(zz, 'r')]
    while len(current) > 0:
        a = current.pop()
        cp = a[0]
        cd = a[1]
        energized.add(cp)
        visited.add(a)      # Tuning tip: it's enough to differentiate if the position was visited horizontally or vertically
#        print()
#        print('cp:', cp)
#        print('current:', current)
#        print('energized:', energized)
        p = slist[cp.row][cp.col]
        directions = move(cd, p)
        for i in directions:
            newpos = Position(cp.row, cp.col)
            newpos.step(i)
            if (newpos, i) in visited:
                pass
            elif newpos.row < 0 or newpos.row >= len(slist) or newpos.col < 0 or newpos.col >= len(slist[0]):
                pass
            else:
                current.append((newpos, i))
    s = len(energized)
    return s

def process(slist: list[str]):
    start = (Position(0, 0), 'r')
    return process0(slist, start)

def process2(slist: list[str]):
    maxe = 0
    nrow = len(slist)
    ncol = len(slist[0])
    for col in range(ncol):
        start = (Position(0, col), 'd')
        r = process0(slist, start)
        if r > maxe: maxe = r
        start = (Position(nrow - 1, col), 'u')
        r = process0(slist, start)
        if r > maxe: maxe = r
    for row in range(nrow):
        start = (Position(row, 0), 'r')
        r = process0(slist, start)
        if r > maxe: maxe = r
        start = (Position(row, ncol - 1), 'l')
        r = process0(slist, start)
        if r > maxe: maxe = r
    return maxe


def score():
    s = 0
    return s