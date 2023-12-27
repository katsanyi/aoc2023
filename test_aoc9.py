import aoc9

def test_readline():
    assert aoc9.readline('0 3 6 9 12 15') == [0, 3, 6, 9, 12, 15]

def test_getdiff():
    assert aoc9.getdiff([0, 3, 6, 9, 12, 15]) == [3, 3, 3, 3,3]
    assert aoc9.getdiff([3, 3, 3, 3]) == [0, 0, 0]
    assert aoc9.getdiff([16, 33, 50, 64, 72]) == [17, 17, 14, 8]
    assert aoc9.getdiff([0, -3, -6]) == [-3, -3]


def test_is_all_null():
    assert aoc9.is_all_null([])
    assert aoc9.is_all_null([0])
    assert aoc9.is_all_null([0, 0])
    assert False == aoc9.is_all_null([0, 3, 6, 9, 12, 15])

def test_processline():
    assert aoc9.processline([0, 3, 6, 9, 12, 15]) == [[0, 3, 6, 9, 12, 15], [3, 3, 3, 3, 3], [0, 0, 0, 0]]
    assert aoc9.processline([1, 3, 6, 10, 15, 21]) == [[1, 3, 6, 10, 15, 21], [2, 3, 4, 5, 6], [1, 1, 1, 1], [0, 0, 0]]
    assert aoc9.processline([1, 3, 6, 10, 15, 21, 28]) == [[1, 3, 6, 10, 15, 21, 28], [2, 3, 4, 5, 6, 7], [1, 1, 1, 1, 1], [0, 0, 0, 0]]
    assert aoc9.processline([10, 13, 16, 21, 30, 45, 68]) == [[10, 13, 16, 21, 30, 45, 68],
 [3, 3, 5, 9, 15, 23],
 [0, 2, 4, 6, 8],
 [2, 2, 2, 2],
 [0, 0, 0]]

def test_set_next():
    ll = aoc9.processline([0, 3, 6, 9, 12, 15])
    aoc9.set_next((ll))
    assert ll[0][-1] == 18
    ll = aoc9.processline([1, 3, 6, 10, 15, 21])
    aoc9.set_next((ll))
    assert ll[0][-1] == 28
    ll = aoc9.processline([10, 13, 16, 21, 30, 45])
    aoc9.set_next((ll))
    assert ll[0][-1] == 68

def test_set_prev():
    ll = aoc9.processline([0, 3, 6, 9, 12, 15])
    aoc9.set_prev((ll))
    assert ll[0][0] == -3

    ll = aoc9.processline([10, 13, 16, 21, 30, 45, 68])
    print()
    print(ll)
    aoc9.set_prev((ll))
    print(ll)
    assert ll[0][0] == 5

def test_score():
    pass

def test_read():
    l,r = aoc9.read(r'C:\py\github\aoc2023\9_.dat')
    assert r == 114
    assert l == 2

def test_read2():
    l,r = aoc9.read(r'C:\py\github\aoc2023\9.dat')
    assert r == 2043677056
    print(l)

