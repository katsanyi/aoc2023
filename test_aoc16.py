import pytest
import aoc16

@pytest.mark.parametrize('start, dir, expected', [
    (aoc16.Position(10, 20), 'l', aoc16.Position(10, 19)),
    (aoc16.Position(10, 20), 'r', aoc16.Position(10, 21)),
    (aoc16.Position(10, 20), 'u', aoc16.Position( 9, 20)),
    (aoc16.Position(10, 20), 'd', aoc16.Position(11, 20))
])
def test_step(start, dir, expected):
    print('expected:', expected)
    start.step(dir)
    print(start)
    assert start == expected

@pytest.mark.parametrize('d, p, expected', [
    ('r', '|', ['u', 'd']),
    ('l', '|', ['u', 'd']),
    ('u', '|', ['u']),
    ('d', '|', ['d']),
    ('r', '-', ['r']),
    ('l', '-', ['l']),
    ('u', '-', ['l', 'r']),
    ('d', '-', ['l', 'r']),
    ('r', '.', ['r']),
    ('l', '.', ['l']),
    ('u', '.', ['u']),
    ('d', '.', ['d']),
    ('r', '\\', ['d']),
    ('l', '\\', ['u']),
    ('u', '\\', ['l']),
    ('d', '\\', ['r']),
    ('r', '/', ['u']),
    ('l', '/', ['d']),
    ('u', '/', ['r']),
    ('d', '/', ['l'])
])
def test_move(d,p,expected):
    assert aoc16.move(d,p) == expected

@pytest.fixture
def slist_():
    return aoc16.read(r'C:\py\github\aoc2023\16_.dat')

@pytest.fixture
def slist():
    return aoc16.read(r'C:\py\github\aoc2023\16.dat')

def test_process(slist_):
    assert aoc16.process(slist_) == 46

def test_process2(slist_):
    assert aoc16.process2(slist_) == 51

def test_process2(slist):
    assert aoc16.process2(slist) == 7313

def test_process(slist):
    print()
    assert aoc16.process(slist) == 7046



