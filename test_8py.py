import x8_wt


def test_readline():
    assert ('AAA',('BBB','CCC')) == x8_wt.readline('AAA = (BBB, CCC)')

def test_processline():
    assert x8_wt.processline('huhu') == 'huhu'

def test_read():
    dir, map = x8_wt.read(r'C:\py\github\aoc2023\8_.dat')
    assert 'LLR' == dir
    assert {'AAA': ('BBB', 'BBB'), 'BBB': ('AAA', 'ZZZ'), 'ZZZ': ('ZZZ', 'ZZZ')} == map

def test_dir():
    dir, map = x8_wt.read(r'C:\py\github\aoc2023\8_.dat')
    assert 'L' == x8_wt.get_dir(0,dir)
    assert 'L' == x8_wt.get_dir(1,dir)
    assert 'R' == x8_wt.get_dir(2,dir)
    assert 'L' == x8_wt.get_dir(3,dir)

def test_score():
    dir, map = x8_wt.read(r'C:\py\github\aoc2023\8_.dat')
    assert 6 == x8_wt.score(dir, map)
    dir, map = x8_wt.read(r'C:\py\github\aoc2023\8.dat')
    s = x8_wt.score(dir, map)
    assert 17873 == s


def test_start_place():
    dir, map = x8_wt.read(r'C:\py\github\aoc2023\8_2.dat')
    assert ['11A', '22A'] == x8_wt.start_place(map)

def test_is_end_place():
    assert x8_wt.is_end_place([])
    assert x8_wt.is_end_place(['AAZ'])
    assert x8_wt.is_end_place(['AAZ','BBZ'])
    assert not x8_wt.is_end_place(['AAZ','BBZ','BBB'])
    assert not x8_wt.is_end_place(['BBB'])

def test_score2():
    dir, map = x8_wt.read(r'C:\py\github\aoc2023\8_.dat')
    assert 6 == x8_wt.score2(dir, map)

def test_score2b():
    pass
    #dir, map = x8_wt.read(r'C:\py\github\aoc2023\8.dat')
    #s = x8_wt.score2(dir, map)
    #assert 17873 == s