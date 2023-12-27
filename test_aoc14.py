import pytest
import aoc14

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

def xtest_read():
    input = aoc14.read(r'C:\py\github\aoc2023\14_.dat')

def xtest_score():
    input = aoc14.read(r'C:\py\github\aoc2023\14_.dat')
    ret = aoc14.process(input)
    assert aoc14.score(ret) == 136

def xtest_score2():
    input = aoc14.read(r'C:\py\github\aoc2023\14.dat')
    ret = aoc14.process(input)
    assert aoc14.score(ret) == 109424

def test_process1():
    input = aoc14.read(r'C:\py\github\aoc2023\14_.dat')
    ret = aoc14.process1(input)
    #aoc14.print_world(ret)

def test_process1():
    input = aoc14.read(r'C:\py\github\aoc2023\14.dat')
    ret = aoc14.process1(input)
    aoc14.score2(ret)
