import pytest
import aoc13

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

@pytest.mark.parametrize('s, expected', [
    ('xx', [1]),
    ('xxx', [1,2]),
    ('xy', []),
    ('x', []),
    ('xxzy', [1]),
    ('xxzyy', [1,4]),
    ('xxxx', [1,2,3])
])
def test_get_axes_s(s, expected):
    assert aoc13.get_axes_s(s) == expected

@pytest.mark.parametrize('s, l, expected', [
    ('xx', [0,1], [1]),
    ('xx', [0], []),
    ('xxxx', [0, 1, 2, 3], [1, 2, 3]),
    ('xxxx', [0, 1], [1]),
    ('xxxx', [3], [3]),
])
def test_get_axes_sl(s, l, expected):
    assert aoc13.get_axes_sl(s,l) == expected

@pytest.mark.parametrize('s, expected', [
    (['xx'], [1]),
    ([
'#.##..##.',
'..#.##.#.',
'##......#',
'##......#',
'..#.##.#.',
'..##..##.',
'#.#.##.#.',
]    , [5] )
])
def test_get_axes_l(s, expected):
    assert aoc13.get_axes_l(s) == expected

def test_read():
    input = aoc13.read(r'C:\github\aoc2023\13_.dat.txt')
    assert input == [['#.##..##.', '..#.##.#.', '##......#', '##......#', '..#.##.#.', '..##..##.', '#.#.##.#.'], ['#...##..#', '#....#..#', '..##..###', '#####.##.', '#####.##.', '..##..###', '#....#..#']]

def test_score0_horizontal():
    input = aoc13.read(r'C:\github\aoc2023\13_.dat.txt')
    assert aoc13.score0(input[0]) == 5

def test_score0_vertical():
    input = aoc13.read(r'C:\github\aoc2023\13_.dat.txt')
    ret = aoc13.score0(input[1])
    assert ret == 400

def test_score():
    input = aoc13.read(r'C:\github\aoc2023\13_.dat.txt')
    s = aoc13.score(input)
    assert s == 405

def test_score_b():
    input = aoc13.read(r'C:\github\aoc2023\13.dat.txt')
    s = aoc13.score(input)
    print(s)
    #assert s == 405