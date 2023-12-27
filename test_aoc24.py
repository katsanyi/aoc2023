import pytest
import aoc24

def test_readline():
    assert aoc24.readline('19, 13, 30 @ -2,  1, -2') == ((19, 13, 30), (-2,  1, -2))
    assert aoc24.readline('18, 19, 22 @ -1, -1, -2') == ((18, 19, 22), (-1,  -1, -2))


def test_value_at():
    assert aoc24.value_at(((19, 13, 30), (-2,  1, -2)), 14.333) == 15.3335

@pytest.mark.parametrize('e1, e2, mn, mx, expected', [
    (((19, 13, 30), (-2,  1, -2)), ((18, 19, 22), (-1,  -1, -2)), 7, 27, True)
])
def xtest_is_intersecting(e1, e2, mn, mx, expected):
    assert aoc24.is_intersecting(e1, e2, mn, mx) == expected

@pytest.mark.parametrize('e1, e2, expected', [
    (((19, 13, 30), (-2,  1, -2)), ((18, 19, 22), (-1,  -1, -2)), True)
])
def xtest_intersection_point(e1, e2, expected):
    r = aoc24.intersection_point(e1, e2)
    assert r == (14.333333333333334, 15.333333333333332)

def test_read():
    slist = aoc24.readfile(r'C:\py\github\aoc2023\24_.dat')
    t = aoc24.read(slist)
    assert t == [((19, 13, 30), (-2, 1, -2)), ((18, 19, 22), (-1, -1, -2)), ((20, 25, 34), (-2, -2, -4)), ((12, 31, 28), (-1, -2, -1)), ((20, 19, 15), (1, -5, -3))]


def xtest_score_():
    print()
    slist = aoc24.readfile(r'C:\py\github\aoc2023\24_.dat')
    l = aoc24.read(slist)
    s = aoc24.score(l, 7, 27)
    assert s == 2


def test_score():
    print()
    slist = aoc24.readfile(r'C:\py\github\aoc2023\24.dat')
    l = aoc24.read(slist)
    s = aoc24.score(l, 200000000000000, 400000000000000)
    assert s == 2
    # 15317 too low
    # 22778 too high