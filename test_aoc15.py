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
    assert input == [('rn', 1), ('cm', 0), ('qp', 3), ('cm', 2), ('qp', 0), ('pc', 4), ('ot', 9), ('ab', 5), ('pc', 0), ('pc', 6), ('ot', 7)]


@pytest.mark.parametrize('s, expected', [
    ('HASH', 52),
    ('rn', 0)
])
def test_hash(s, expected):
    assert aoc15.hash(s) == expected

@pytest.fixture
def input_():
    return aoc15.read(r'C:\py\github\aoc2023\15_.dat')

@pytest.mark.parametrize('input, expected, comment', [
    ([('rn', 1)], [[('rn',1)],[]],'Adding to box 0'),
    ([('rn', 1),('cm', 0)],                                     [[('rn', 1)], []],                      'Nothing to remove'),
    ([('rn', 1), ('cm', 0), ('qp',3)], [[('rn', 1)],            [('qp',3)]],                            'Adding to box 1'),
    ([('rn', 1), ('cm', 0), ('qp', 3),('cm',2)],                [[('rn', 1), ('cm', 2)], [('qp', 3)]],  'Add 2nd lens to box 0'),
    ([('rn', 1), ('cm', 0), ('qp', 3), ('cm', 2), ('qp',0)],    [[('rn', 1), ('cm', 2)], []],           'Removing lens'),
    ([('rn', 1), ('cm', 0), ('qp', 3), ('cm', 2),('rn',3)], [[('rn', 3), ('cm', 2)], [('qp', 3)]], 'Replacing lens 0'),
])
def test_process_box0(input, expected, comment):
    r = aoc15.process(input)
    assert r[0] == expected[0]
    assert r[1] == expected[1]

@pytest.fixture
def processed_input_():
#def processed_input_(input_):
    input_ = aoc15.read(r'C:\py\github\aoc2023\15_.dat')
    pi = aoc15.process(input_)
    return pi


def test_focus_power(processed_input_):
    assert aoc15.focus_power(processed_input_[0],0) == 5
    assert aoc15.focus_power(processed_input_[3],3) == 140

def test_score(input_):
    input_ = aoc15.read(r'C:\py\github\aoc2023\15_.dat')
    pi = aoc15.process(input_)
    sc = aoc15.score(pi)
    assert sc == 145

def test_scoreb():
    input = aoc15.read(r'C:\py\github\aoc2023\15.dat')
    pi = aoc15.process(input)
    sc = aoc15.score(pi)
    assert sc == 247763

def xtest_score_r():
    input = aoc15.read(r'C:\py\github\aoc2023\15.dat')
    assert aoc15.score(input) == 1320

