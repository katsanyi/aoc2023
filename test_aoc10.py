import aoc10

def test_move():
    world = aoc10.read(r'C:\py\github\aoc2023\10_.dat')
    print()
    aoc10.print_world(world)
    #aoc10.move(world,(0,2),'d')
    assert 1 == 1

def test_findS():
    world = aoc10.read(r'C:\py\github\aoc2023\10_.dat')
    spos = aoc10.findS(world)
    assert spos[0] == 2
    assert spos[1] == 1

def test_go():
    world = aoc10.read(r'C:\py\github\aoc2023\10_.dat')
    spos = aoc10.findS(world)
    c,loop = aoc10.go(world,spos,'d')
    assert 4 == round(c)

def test_count_enclosed():
    return
    world = aoc10.read(r'C:\py\github\aoc2023\10_.dat')
    spos = aoc10.findS(world)
    c,loop = aoc10.go(world,spos,'d')
    s = aoc10.count_enclosed(world, loop)
    assert 1 == s

def test_count_enclosed2():
    world = aoc10.read(r'C:\py\github\aoc2023\10_2.dat')
    spos = aoc10.findS(world)
    c,loop = aoc10.go(world,spos,'d')
    s = aoc10.count_enclosed(world, loop)
    assert 4 == s
# 1132 is too high

def test_count_enclosed2():
    world = aoc10.read(r'C:\py\github\aoc2023\10.dat')
    spos = aoc10.findS(world)
    c,loop = aoc10.go(world,spos,'d')
    s = aoc10.count_enclosed(world, loop)
    assert 4 == s
# 1132 is too high

def test_go2():
    world = aoc10.read(r'C:\py\github\aoc2023\10.dat')
    spos = aoc10.findS(world)
    c, loop = aoc10.go(world,spos,'d')
    assert 6870 == round(c)


def test_score():
    pass

def test_read():
    aoc10.read(r'C:\py\github\aoc2023\10_.dat')
    assert 1 == 1

def test_read2():
    aoc10.read(r'C:\py\github\aoc2023\10.dat')
    assert 1 == 1

