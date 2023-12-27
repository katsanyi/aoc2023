import re
import copy
import sys

print(r'Processing...')
# tuple: hand (orig form), bid, cardinality, type, hand (converted to comparable string)
hands = []

#reads the file, returns as list, strips end of line and end of file chars, no other transformation
def readfile(fname):
    s=[]
    with open(fname) as f:
        while True:
            line = f.readline()
            if not line:
                break
            s.append(line.strip())
    return s

def myassert(a,b):
    if a != b:
        print('Assertion failed', a, ' != ',b)


def readline(line):
    parts = re.split(' ', line)
    return (parts[0],int(parts[1]))

def test_readline():
    myassert(('32T3K',765),readline('32T3K 765'))

test_readline()

def processline(game):
    hand0 = game[0]
    bid = game[1]
    if 'JJJJJ' == hand0:
        return ('JJJJJ',bid,[5],'5','0000000000', '70000000000')
    hand = {i: hand0.count(i) for i in hand0}
    if 'J' in hand:
        countj = hand['J']
        hand.pop('J')
    else:
        countj=0
    handc = list(hand.values())
    handc.sort(reverse=True)
    handc[0] += countj
    if 5 == handc[0]:
        type = '5'
        key = '7'
    elif 4 == handc[0]:
        type = '4'
        key = '6'
    elif 3 == handc[0] and 2 == handc[1]:
        type = '32'
        key = '5'
    elif 3 == handc[0]:
        type = '3'
        key = '4'
    elif 2 == handc[0] and 2 == handc[1]:
        type = '22'
        key = '3'
    elif 2 == handc[0]:
        type = '2'
        key = '2'
    else:
      type = '1'
      key = '1'
    handv = ''
    for i in hand0:
        if 'A' == i:
            v = '14'
        elif 'K' == i:
            v = '13'
        elif 'Q' == i:
            v = '12'
        elif 'J' == i:
            v = '00' #!
        elif 'T' == i:
            v = '10'
        else:
            v = '0'+i
        handv += v
    key += handv

    return (hand0, bid, handc, type, handv,key)

def test_processline():
    myassert(('32T3K',765,[2,1,1,1],'2','0302100313', '20302100313'),processline(('32T3K',765)))
    myassert(('T55J5',765,[4,1]  ,'4','1005050005', '61005050005'),processline(('T55J5',765)))
    myassert(('KK677',765,[2,2,1] ,'22','1313060707', '31313060707'),processline(('KK677',765)))
    myassert(('KTJJT',765,[4,1] ,'4','1310000010',  '61310000010'),processline(('KTJJT',765)))
    myassert(('QQQJA',765,[4,1]  ,'4','1212120014', '61212120014'),processline(('QQQJA',765)))
    myassert(('5'),processline(('QQQJQ',765))[3])
    myassert(('5'),processline(('QQQQQ',765))[3])
    myassert(('32'),processline(('QQQAA',765))[3])
    myassert(('32'),processline(('QQAAA',765))[3])
    myassert(('22'),processline(('QxQAA',765))[3])
    myassert(('71212120012'),processline(('QQQJQ',765))[5])
    myassert(('71212121212'),processline(('QQQQQ',765))[5])

test_processline()

def read(fname):
    global hands
    hands = []
    fc = readfile(fname)
    for i in fc:
        h = processline(readline(i))
        hands.append(processline(h))

def test_read():
    read(r'C:\py\github\aoc2023\7_.dat')
    #myassert([('32T3K', 765, [2, 1, 1, 1], '2', '0302100313', '20302100313'), ('T55J5', 684, [3, 1, 1], '3', '1005051105', '41005051105'), ('KK677', 28, [2, 2, 1], '22', '1313060707', '31313060707'), ('KTJJT', 220, [2, 2, 1], '22', '1310111110', '31310111110'), ('QQQJA', 483, [3, 1, 1], '3', '1212121114', '41212121114')], hands)

test_read()



def score():
    print(hands)
    sorted_hands = sorted(hands,key=lambda x: x[5])
    print(sorted_hands)
    s = 0
    for i in range(len(sorted_hands)):
        s += (i + 1) * sorted_hands[i][1]
    return s

s = score()
print(s)


read(r'C:\py\github\aoc2023\7.dat')
print(score())
sys.exit(0)

read(r'C:\py\github\aoc2023\6.dat')
print(score())

read(r'C:\py\github\aoc2023\6_b.dat')
print(score())

read(r'C:\py\github\aoc2023\6b.dat')
print(score())
