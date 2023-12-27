import pytest
import aoc16

@pytest.mark.parametrize('d, p, expected', [
    ('r', '.', 'r'),
    ('l', '.', 'l'),
    ('u', '.', 'u'),
    ('d', '.', 'd'),
    ('r', '\\', 'd'),
    ('l', '\\', 'u'),
    ('u', '\\', 'l'),
    ('d', '\\', 'r'),
    ('r', '/', 'u'),
    ('l', '/', 'd'),
    ('u', '/', 'r'),
    ('d', '/', 'l')
])
def test_move(d,p,expected):
    assert aoc16.move(d,p,0,0) == expected

def xtest_score1():
    assert aoc15.score1('HASH') == 52

def xtest_score():
    input = aoc15.read(r'C:\py\github\aoc2023\16_.dat')
    assert aoc15.score(input) == 1320



