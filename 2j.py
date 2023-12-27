d1 = {
    "A": 1,
    "B": 2,
    "C": 3
}
d2 = {
    "X": 1,
    "Y": 2,
    "Z": 3
}
rps = {
    1: "Rock",
    2: "Paper",
    3: "Scissors"
}
rps1 = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3
}
abc = 'ABC'
xyz = 'XYZ'
# Reads file named fname, returns content in list of strings
# Todo: handle exceptions
def readfile(fname):
    s=[]
    with open(r'c:\py\advent of code\2.dat ') as f:
        while True:
            line = f.readline()
            if not line:
                break
            s.append(line)
    return s

# Parses a line
# Todo: validate input
def parseline(line):
    a = line[0]
    b = line[2]
    return a,b

# a and b are either Rock, Paper and Scissors, returns draw / me / opp as per the rules of the game
# Todo: validate input
def basic_game(a,b):
    if a == b: winner = 'draw'
    elif a == 'Rock' and b == 'Paper': winner = 'me'
    elif a == 'Paper' and b == 'Scissors': winner = 'me'
    elif a == 'Scissors' and b == 'Rock': winner = 'me'
    else: winner = 'opp'
    return winner

# a is A, B or C, b is X, Y or Z, returns draw / me / opp as per the rules of the game
# Todo: validate input
def game(a,b):
    aa = rps[d1[a]]
    bb = rps[d2[b]]
    return basic_game(aa,bb)

# a is A, B or C, b is X, Y or Z, returns score
def score(a,b):
    winner = game(a,b)
    if winner == 'opp':
        r=0
    elif winner == 'me':
        r=6
    else:
        r=3
    return r+d2[b]

def calc():
    r = 0
    s = 0
    fc = readfile(r'c:\py\advent of code\2.dat')
    for line in fc:
        a, b = parseline(line)
        s += score(a,b)
    return s

def myassert(a,b):
    if a != b:
        print('Assertion failed', a, ' != ',b)

#myassert('a','b')
#myassert('a','a')

myassert(basic_game('Rock','Rock'),'draw')
myassert(basic_game('Paper','Paper'),'draw')
myassert(basic_game('Scissors','Scissors'),'draw')
myassert(basic_game('Rock','Paper'),'me')
myassert(basic_game('Paper','Scissors'),'me')
myassert(basic_game('Scissors','Rock'),'me')
myassert(basic_game('Rock','Scissors'),'opp')
myassert(basic_game('Paper','Rock'),'opp')
myassert(basic_game('Scissors','Paper'),'opp')

# Asserting that playing with ABC / XYZ gives the same results as the corresponding basic game
for i in ['Rock', 'Paper', 'Scissors']:
    for j in ['Rock', 'Paper', 'Scissors']:
        myassert(basic_game(i,j), game(abc[rps1[i] - 1], xyz[rps1[j] - 1]))
        if i == 'Rock' and j == 'Rock':         myassert(score(abc[rps1[i] - 1], xyz[rps1[j] - 1]),4)
        if i == 'Paper' and j == 'Paper':       myassert(score(abc[rps1[i] - 1], xyz[rps1[j] - 1]),5)
        if i == 'Scissors' and j == 'Scissors': myassert(score(abc[rps1[i] - 1], xyz[rps1[j] - 1]),6)
        if i == 'Rock' and j == 'Paper':        myassert(score(abc[rps1[i] - 1], xyz[rps1[j] - 1]),8)
        if i == 'Paper' and j == 'Scissors':    myassert(score(abc[rps1[i] - 1], xyz[rps1[j] - 1]),9)
        if i == 'Scissors' and j == 'Rock':     myassert(score(abc[rps1[i] - 1], xyz[rps1[j] - 1]),7)
        if i == 'Rock' and j == 'Scissors':     myassert(score(abc[rps1[i] - 1], xyz[rps1[j] - 1]),3)
        if i == 'Paper' and j == 'Rock':        myassert(score(abc[rps1[i] - 1], xyz[rps1[j] - 1]),1)
        if i == 'Scissors' and j == 'Paper':    myassert(score(abc[rps1[i] - 1], xyz[rps1[j] - 1]),2)



myassert(game('A','X'),'draw')
myassert(game('B','Y'),'draw')
myassert(game('C','Z'),'draw')
myassert(game('A','Y'),'me')
myassert(game('B','Z'),'me')
myassert(game('C','X'),'me')

myassert(game('A','X'),'draw')



s=calc()
if s != 13924:
    print('main test failed')
else:
    print('All good')
print(s)

# Todo: make it BDD: 9 variations of ABC/XYZ, rps, me/opp/draw, score
# or maybe not
# define score ot rps level
# assert rps (9 variations of rps, me/opp/draw, score
# assert map from abc to rps