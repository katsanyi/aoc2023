import pytest
import aoc13b

@pytest.mark.parametrize('s1, s2, expected', [
    ('xx', 'xx', 0),
    ('xx', 'xy', 1),
    ('xx', 'yy', 2)
])
def test_diff(s1, s2, expected):
    assert aoc13b.diff(s1,s2) == expected


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
def xtest_is_symmetric(s, p, expected):
    assert aoc13b.is_symmetric(s,p) == expected

@pytest.mark.parametrize('s, expected', [
    ('xx', [[1,0]]),
    ('xxx', [[1,0],[2,0]]),
    ('xy', [[1,1]]),
    ('x', []),
    ('xxzy', [[1,0],[2,2],[3,1]]),
    ('xxzyy', [[1,0],[2,2],[3,2],[4,0]]),
    ('xxxx', [[1,0],[2,0],[3,0]])
])
def test_get_axes_s(s, expected):
    assert aoc13b.get_axes_s(s) == expected

@pytest.mark.parametrize('s, expected', [
    (['xx'], [1]),   #           [[1,0]]),
    ([
'#.##..##.',
'..#.##.#.',
'##......#',
'##......#',
'..#.##.#.',
'..##..##.',
'#.#.##.#.',
]    , [5]) #  [[1, 2], [2, 11], [3, 13], [4, 16], [5, 0], [6, 11], [7, 8], [8, 7]] )
])
def test_get_axes_l(s, expected):
    r = aoc13b.get_axes_l(s)
    print()
    print(r, expected)
    assert r == expected

def test_read():
    input = aoc13b.read(r'C:\py\github\aoc2023\13_.dat.txt')
    assert input == [['#.##..##.', '..#.##.#.', '##......#', '##......#', '..#.##.#.', '..##..##.', '#.#.##.#.'], ['#...##..#', '#....#..#', '..##..###', '#####.##.', '#####.##.', '..##..###', '#....#..#']]

def test_score0_horizontal():
    input = aoc13b.read(r'C:\py\github\aoc2023\13_.dat.txt')
    assert aoc13b.score0(input[0]) == 5

def test_score0_vertical():
    input = aoc13b.read(r'C:\py\github\aoc2023\13_.dat.txt')
    ret = aoc13b.score0(input[1])
    assert ret == 400

def test_score():
    input = aoc13b.read(r'C:\py\github\aoc2023\13_.dat.txt')
    s = aoc13b.score(input)
    assert s == 405

def test_score_b():
    input = aoc13b.read(r'C:\py\github\aoc2023\13.dat.txt')
    s = aoc13b.score(input)
    print(s)
    #assert s == 405