import aoc12
import aoc12.fivetimes


def test_fivetimes():
    assert aoc12.fivetimes('') == '????'
    assert aoc12.fivetimes('x') == 'x?x?x?x?x'


def test_readline():
    assert aoc12.readline('???.### 1,1,3') == ('???.###', [1, 1, 3])

def test_lenlist():
    assert aoc12.lenlist('#.#.###') == [1,1,3]
    assert aoc12.lenlist('#.#.###.') == [1,1,3]
    assert aoc12.lenlist('.#.#.###.') == [1,1,3]
    assert aoc12.lenlist('.') == []
    assert aoc12.lenlist('') == []
    assert aoc12.lenlist('#') == [1]

def test_fits():
    assert aoc12.fits('#.#.###', '???.###') == True
    assert aoc12.fits('#.#.###', '#.#.###') == True
    assert aoc12.fits('#.#.###', '#?#.###') == True
    assert aoc12.fits('#.#.###', '#.?.##?') == True
    assert aoc12.fits('#.#.###.', '???.###') == False
    assert aoc12.fits('#.#.###', '???.###.') == False

def test_fullfits():
    assert aoc12.full_fits('#.#.###', '???.###',[1,1,3]) == True
    assert aoc12.full_fits('#.#.###', '???.###',[1,1,2]) == False
    assert aoc12.full_fits('#.#.###', '???.###',[1,1]) == False
    assert aoc12.full_fits('#.#.###', '???.###',[1,1,3,1]) == False

def test_can_be_good():
    assert aoc12.can_be_good('#.#.###', '???.###',[1,1,3]) == True
    assert aoc12.can_be_good('#.#.###', '???.###',[1,1,3,1]) == False
    assert aoc12.can_be_good('#.#.##', '???.###',[1,1,3]) == True
    assert aoc12.can_be_good('#.#.#.', '???.###',[1,1,3]) == False
    assert aoc12.can_be_good('', '??????#????#.?#???#', [1,1,3,1,3,1]) == True

def test_no_good():
    assert aoc12.no_good('', '???.###',[1,1,3]) == 1
    assert aoc12.no_good('', '.??..??...?##.',[1,1,3]) == 4
    assert aoc12.no_good('', '?###????????', [3, 2, 1]) == 10
    assert aoc12.no_good('', '???.###????.###????.###????.###????.###', [1,1,3,1,1,3,1,1,3,1,1,3,1,1,3]) == 1
    assert aoc12.no_good('', fivetimes('?#?#?#?#?#?#?#?'), [1,3,1,6]*5) == 1
    assert aoc12.no_good('', fivetimes('.??..??...?##.'), [1,1,3]*5) == 16384





def test_read():
    aoc12.read(r'C:\py\github\aoc2023\12_.dat')
    assert 1 == 1

def test_score():
    input = aoc12.read(r'C:\py\github\aoc2023\12_.dat')
    assert aoc12.score(input) == 21

def test_score_b():
    input = aoc12.read(r'C:\py\github\aoc2023\12_.dat')
    i2 = []
    for i in input:
        i2.append((fivetimes(i[0]),i[1]*5))
    #assert aoc12.score(i2) == 525152


def test_score2():
    input = aoc12.read(r'C:\py\github\aoc2023\12.dat')
    assert aoc12.score(input) == 7307