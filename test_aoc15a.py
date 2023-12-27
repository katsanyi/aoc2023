import pytest
import aoc15

'''
@pytest.mark.parametrize('s, p, expected', [
    ('xx', 10, False),
    ('xx', 0, False),
    ('xx', 1, True),
    ('xxx', 1, True),
    ('xxx', 2, True),
    ('xxyz', 1, True),
    ('xxxx', 2, True),
    ('yzxx', 3, True),
    ('xxxy', 2, False)
])
def test_is_symmetric(s, p, expected):
    assert aoc13.is_symmetric(s,p) == expected
'''

def test_read():
    input = aoc15.read(r'C:\py\github\aoc2023\15_.dat')
    assert input == ['rn=1', 'cm-', 'qp=3', 'cm=2', 'qp-', 'pc=4', 'ot=9', 'ab=5', 'pc-', 'pc=6', 'ot=7']

def test_score1():
    assert aoc15.score1('HASH') == 52

def test_score():
    input = aoc15.read(r'C:\py\github\aoc2023\15_.dat')
    assert aoc15.score(input) == 1320

def test_score_r():
    input = aoc15.read(r'C:\py\github\aoc2023\15.dat')
    assert aoc15.score(input) == 1320

