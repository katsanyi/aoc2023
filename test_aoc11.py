import aoc11

def test_is_empty_row():
    fc = aoc11.readfile(r'C:\py\github\aoc2023\11_.dat')
    assert aoc11.is_empty_row(fc,0) == False
    assert aoc11.is_empty_row(fc,1) == False
    assert aoc11.is_empty_row(fc,3) == True

def test_is_empty_col():
    fc = aoc11.readfile(r'C:\py\github\aoc2023\11_.dat')
    assert aoc11.is_empty_col(fc,0) == False
    assert aoc11.is_empty_col(fc,1) == False
    assert aoc11.is_empty_col(fc,2) == True
    assert aoc11.is_empty_col(fc,3) == False
    assert aoc11.is_empty_col(fc,5) == True

def test_get_dist():
    assert aoc11.get_dist((2,2),(2,2)) == 0
    assert aoc11.get_dist((2,2),(2,1)) == 1
    assert aoc11.get_dist((2,2),(2,3)) == 1
    assert aoc11.get_dist((2,2),(1,1)) == 2


def test_get_coords():
    fc = aoc11.readfile(r'C:\py\github\aoc2023\11_.dat')
    pworld = aoc11.get_coords(fc,2)
    assert pworld == [(0, 4), (1, 9), (2, 0), (5, 8), (6, 1), (7, 12), (10, 9), (11, 0), (11, 5)]
    assert aoc11.get_dist(pworld[0],pworld[6]) == 15
    assert aoc11.get_dist(pworld[2],pworld[5]) == 17
    assert aoc11.get_dist(pworld[7],pworld[8]) == 5

def test_score():
    fc = aoc11.readfile(r'C:\py\github\aoc2023\11.dat')
    pworld = aoc11.get_coords(fc,2)
    s = aoc11.score(pworld)
    assert s == 10490062

def test_score2():
    fc = aoc11.readfile(r'C:\py\github\aoc2023\11.dat')
    pworld = aoc11.get_coords(fc,1000000)
    s = aoc11.score(pworld)
    assert s == 382979724122