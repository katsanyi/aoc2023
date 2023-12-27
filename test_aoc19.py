import pytest
import aoc19

@pytest.mark.parametrize('s', [
    ('a<2006:qkq'),
    ('a>2006:R'),
    ('A')
])
def test_rule(s):
    r = aoc19.rule(s)
    assert str(r) == s

@pytest.mark.parametrize('s', [
    ('gd{R}'),
    ('gd{a>3333:R}'),
    ('gd{a>3333:R,R}')
])
def test_ruleset(s):
    r = aoc19.ruleset(s)
    assert str(r) == s


@pytest.mark.parametrize('s', [
    ('{x=787,m=2655,a=1222,s=2876}'),
    ('{x=2127,m=1623,a=2188,s=1013}')
])
def test_part_init(s):
    r = aoc19.part(s)
    assert str(r) == s

@pytest.mark.parametrize('s, expected', [
    ('{x=1,m=2,a=3,s=4}', 10)
])
def test_part_score(s, expected):
    r = aoc19.part(s)
    assert r.score() == expected
'''
@pytest.mark.parametrize('sl,rsl, pl', [
    (['px{a<2006:qkq,m>2090:A,rfg}','', '{x=787,m=2655,a=1222,s=2876}'], 1, 1),
    (['px{a<2006:qkq,m>2090:A,rfg}','cx{a<2006:qkq,m>2090:A,rfg}', '', '{x=787,m=2655,a=1222,s=2876}'], 2, 1),
    (['px{a<2006:qkq,m>2090:A,rfg}', 'cx{a<2006:qkq,m>2090:A,rfg}', '', '{x=787,m=2655,a=1222,s=2876}', '{x=7,m=2655,a=1222,s=2876}'], 2, 2)
])
def test_read(sl, rsl, pl):
    (rulesets, parts) = aoc19.read(sl)
    for i in range(rsl):
        assert str(rulesets[i]) == sl[i]
    for i in range(pl):
        assert str(parts[i]) == sl[i + rsl + 1]
'''
@pytest.mark.parametrize('sl,rsl, pl', [
    (['px{a<2006:qkq,m>2090:A,rfg}','', '{x=787,m=2655,a=1222,s=2876}'], ['px'], 1),
    (['px{a<2006:qkq,m>2090:A,rfg}','cx{a<2006:qkq,m>2090:A,rfg}', '', '{x=787,m=2655,a=1222,s=2876}'], ['px','cx'], 1),
    (['px{a<2006:qkq,m>2090:A,rfg}', 'cx{a<2006:qkq,m>2090:A,rfg}', '', '{x=787,m=2655,a=1222,s=2876}', '{x=7,m=2655,a=1222,s=2876}'], ['px','cx'], 2)
])
def test_read(sl, rsl, pl):
    (rulesets, parts) = aoc19.read(sl)
    for i in range(len(rsl)):
        #print('i',i, rsl[i], rulesets[rsl[i]])
        s = ''
        assert str(rulesets[rsl[i]]) == sl[i]
    #for i in range(rsl): assert str(rulesets[i]) == sl[i]
    for i in range(pl):
        assert str(parts[i]) == sl[i + len(rsl) + 1]


@pytest.mark.parametrize('srset, p, expected', [
    ('px{A}', '{x=787,m=2655,a=1222,s=2876}', 'A'),
    ('px{pq}', '{x=787,m=2655,a=1222,s=2876}', 'pq'),
    ('px{a<2006:qkq,m>2090:A,rf}', '{x=787,m=2655,a=1222,s=2876}', 'qkq'),
    ('px{a<2006:qkq,m>2090:A,rf}', '{x=787,m=2655,a=12220,s=2876}', 'A'),
    ('px{a<2006:qkq,m>2090:A,rf}', '{x=787,m=655,a=12202,s=2876}', 'rf')
    #        ('px{a<2006:qkq,m>2090:A,rfg}', '', '{x=787,m=2655,a=1222,s=2876}'], 'qkq')

])
def test_evaluate_ruleset(srset: str, p: str, expected:str):
    rset = aoc19.ruleset(srset)
    part = aoc19.part(p)
    rsname = aoc19.evaluate_ruleset(rset, part)
    assert rsname == expected

def test_process1part():
    sl = aoc19.readfile(r'C:\py\github\aoc2023\19_.dat')
    (rulesets, parts) = aoc19.read(sl)
    assert aoc19.process1part(rulesets, parts[0]) == 'A'
    assert aoc19.process1part(rulesets, parts[1]) == 'R'


def test_process_():
    sl = aoc19.readfile(r'C:\py\github\aoc2023\19_.dat')
    (rulesets, parts) = aoc19.read(sl)
    s = aoc19.process(rulesets, parts)
    assert s == 19114

def test_process():
    sl = aoc19.readfile(r'C:\py\github\aoc2023\19.dat')
    (rulesets, parts) = aoc19.read(sl)
    s = aoc19.process(rulesets, parts)
    assert s == 333263

def test_reachable():
    sl = aoc19.readfile(r'C:\py\github\aoc2023\19_.dat')
    (rsets, parts) = aoc19.read(sl)
    s = aoc19.reachable(rsets)
    # no need to assert

def test_get_paths():
    sl = aoc19.readfile(r'C:\py\github\aoc2023\19_.dat')
    (rsets, parts) = aoc19.read(sl)
    s = aoc19.gen_paths(rsets)
    # no need to assert
