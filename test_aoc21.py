import pytest
import aoc21

@pytest.mark.parametrize('s, expected', [
    ('.#',(['.','#'], -1)),
    ('.S', (['.', '.'], 1))
])
def test_readline(s, expected):
    r = aoc21.readline(s)
    assert r == expected

@pytest.fixture
def input_():
    slist = aoc21.readfile(r'C:\py\github\aoc2023\21_.dat')
    input_ = aoc21.read(slist)
    return input_

@pytest.fixture
def input():
    slist = aoc21.readfile(r'C:\py\github\aoc2023\21.dat')
    input_ = aoc21.read(slist)
    return input_

def test_read(input_):
    assert input_ == ([['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
  ['.', '.', '.', '.', '.', '#', '#', '#', '.', '#', '.'],
  ['.', '#', '#', '#', '.', '#', '#', '.', '.', '#', '.'],
  ['.', '.', '#', '.', '#', '.', '.', '.', '#', '.', '.'],
  ['.', '.', '.', '.', '#', '.', '#', '.', '.', '.', '.'],
  ['.', '#', '#', '.', '.', '.', '#', '#', '#', '#', '.'],
  ['.', '#', '#', '.', '.', '#', '.', '.', '.', '#', '.'],
  ['.', '.', '.', '.', '.', '.', '.', '#', '#', '.', '.'],
  ['.', '#', '#', '.', '#', '.', '#', '#', '#', '#', '.'],
  ['.', '#', '#', '.', '.', '#', '#', '.', '#', '#', '.'],
  ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']],
 (5, 5))

def test_step(input_):
    current = [input_[1]]
    assert aoc21.step(input_[0], current) == [(5,4), (4,5)]

def xtest_nstep(input_):
    s = aoc21.nstep(input_, 6)
    assert s == 16

def test_nstep(input):
    s = aoc21.nstep(input, 64)
    assert s == 16