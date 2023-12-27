import pytest
import aoc18

def test_readline():
    assert aoc18.readline('R 10 (#3180b0)') == ('R',10)

def test_read():
    input = ['R 10 (#3180b0)', 'L 1 (#3180b0)']
    assert aoc18.read(input) == [('R',10), ('L',1)]


@pytest.mark.parametrize('slist, expected', [
    ([],{(0,0)}),
    ([('R',2)], {(0, 0),(0, 1),(0, 2)}),
    ([('R',2),('R', 0)], {(0, 0), (0, 1), (0, 2), }),
    ([('R', 1), ('R', 1)], {(0, 0), (0, 1), (0, 2), }),
    ([('R', 1), ('D', 1)], {(0, 0), (0, 1), (1, 1), }),
    ([('R', 1), ('D', 2),('L',1)], {(0, 0), (0, 1), (1, 1), (2, 1), (2, 0), }),
    ([('R', 1), ('D', 2),('L',1),('U',1)], {(0, 0), (0, 1), (1, 1), (2, 1), (2, 0),(1,0) })
])
def test_process0(slist, expected):
    assert aoc18.process(slist).keys() == expected

#todo: add test cases for the characters
@pytest.fixture
def tset_():
    slist = aoc18.readfile(r'C:\py\github\aoc2023\18_.dat')
    tlist_ = aoc18.read(slist)
    tset_ = aoc18.process(tlist_)
    return tset_

@pytest.fixture
def tset():
    slist = aoc18.readfile(r'C:\py\github\aoc2023\18.dat')
    tlist = aoc18.read(slist)
    tset = aoc18.process(tlist)
    return tset

def test_process3(tset_):
    slist = aoc18.readfile(r'C:\py\github\aoc2023\18_.dat')
    tlist_ = aoc18.read(slist)
    (poligon, perim) = aoc18.process3(tlist_)
#    print(poligon)
    print('Perimeter:', perim)

def test_process_(tset_):
    plist = aoc18.process2(tset_)
    assert plist  == 62

def xtest_process(tset):
    plist = aoc18.process2(tset)
    assert plist == 70026

@pytest.mark.parametrize('vlist, expected', [
    ([(0,0),(0,1),(1,0)],0.5),
    ([(0, 0), (0, 2), (2, 0)], 2),
    ([(0, 0), (0, 1), (1, 0), (1,0)], 20),
    ([(0, 0), (0, 2), (2,2), (2, 0)], 4),
    ([(0, 0), (0, 3), (3, 3), (3, 0)], 40),
    ([(0, 0), (0, 4), (4, 4), (4, 0)], 50),
    ([(0, 0), (0, 2), (2,2), (2, 1), (2, 0)], 4),
    ([(0, 0), (0, 2), (2, 2), (2, 1), (3,1), (3,0)], 6)
])
def xtest_shoelace0(vlist, expected):
    area = aoc18.shoelace(vlist)
    assert area == expected

def test_shoelace_():
    slist = aoc18.readfile(r'C:\py\github\aoc2023\18_.dat')
    tlist_ = aoc18.read(slist)
    (poligon, perim) = aoc18.process3(tlist_)
#    print(poligon)
    netarea = aoc18.shoelace(poligon)
    area = netarea + perim / 2 + 1
    assert area == 62

def test_shoelace():
    slist = aoc18.readfile(r'C:\py\github\aoc2023\18.dat')
    tlist_ = aoc18.read(slist)
    (poligon, perim) = aoc18.process3(tlist_)
#    print(poligon)
    netarea = aoc18.shoelace2(poligon)
    area = netarea + perim / 2 + 1
    assert area == 70026

@pytest.mark.parametrize('s, expected', [
    ('R 6 (#70c710)', ('R', 461937)),
    ('R 6 (#0dc571)', ('D', 56407)),
    ('R 6 (#8ceee2)', ('L', 577262)),
    ('R 6 (#caa173)', ('U', 829975))
])
def test_readline2(s, expected):
    assert aoc18.readline2(s) == expected

def test_shoelace2_():
    slist = aoc18.readfile(r'C:\py\github\aoc2023\18_.dat')
    tlist_ = aoc18.read2(slist)
#    print(tlist_)
    (poligon, perim) = aoc18.process3(tlist_)
#    print(poligon)
#    print(perim)
    netarea = aoc18.shoelace2(poligon)
    area = netarea + perim / 2 + 1
    assert area == 952408144115

def test_shoelace2():
    slist = aoc18.readfile(r'C:\py\github\aoc2023\18.dat')
    tlist_ = aoc18.read2(slist)
    (poligon, perim) = aoc18.process3(tlist_)
    netarea = aoc18.shoelace2(poligon)
    area = netarea + perim / 2 + 1
    assert area == 68548301037382