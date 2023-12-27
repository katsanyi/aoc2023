print(r'Processing...')

digits = '0123456789'
digitsperiod = '0123456789.'
numbers = []
symbols = []

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

def find_numbers(s):
    n=0
    j=0
    start=0
    ret=[]
    s += '/'
    for i in s:
        if digits.count(i)>0:
          n = 10*n + int(i)
        else:
            if n > 0:
              ret.append([n,start,j-1,False])
              n=0
            start = j+1
        j += 1
    return ret

def find_symbols(s):
    j=0
    ret=[]
    for i in s:
        if digitsperiod.count(i) == 0:
          ret.append(j)
        j += 1
    return ret

def find_stars(s):
    j=0
    ret=[]
    for i in s:
        if i == '*':
          ret.append(j)
        j += 1
    return ret

#assumption: first and last line does not contain symbols
def process(fname):
    r = 0
    s = 0
    fc = readfile(fname)
    for line in fc:
        numbers.append(find_numbers(line))
        symbols.append(find_symbols(line))
    ii = 0
    for i in symbols:
        for j in i:
            for k in numbers[ii-1]:
                if not (k[1] > j + 1 or k[2] < j - 1):
                    k[3] = True
            for k in numbers[ii]:
                if not (k[1] > j + 1 or k[2] < j - 1):
                    k[3] = True
            for k in numbers[ii + 1]:
                if not (k[1] > j + 1 or k[2] < j - 1):
                    k[3] = True
        ii += 1
    for i in numbers:
        for j in i:
            if j[3]:
                s += j[0]
            else:
                print(j[0])
    return s

def process2(fname):
    r = 0
    s = 0
    fc = readfile(fname)
    for line in fc:
        numbers.append(find_numbers(line))
        symbols.append(find_symbols(line))
    ii = 0
    for i in symbols:
        for j in i:
            multipliers = []
            for k in numbers[ii-1]:
                if not (k[1] > j + 1 or k[2] < j - 1):
                    multipliers.append(k[0])
            for k in numbers[ii]:
                if not (k[1] > j + 1 or k[2] < j - 1):
                    multipliers.append(k[0])
            for k in numbers[ii + 1]:
                if not (k[1] > j + 1 or k[2] < j - 1):
                    multipliers.append(k[0])
            print(len(multipliers), ' ', multipliers)
            if len(multipliers) == 2:
                s += multipliers[0] * multipliers[1]
        ii += 1
    for i in numbers:
        for j in i:
            if j[3]:
                s += j[0]
            else:
                pass
                #print(j[0])
    return s

def test_find_numbers():
    myassert([[1, 0, 0,False]],find_numbers('1'))
    myassert([],find_numbers('q'))
    myassert([],find_numbers('0'))
    myassert([[1234567890, 0, 9,False]],find_numbers('1234567890'))
    myassert([[1234567, 0, 6,False], [890, 8, 10,False]],find_numbers('1234567-890'))

def test_find_symbols():
    myassert([],find_symbols(''))
    myassert([0],find_symbols('x'))
    myassert([2],find_symbols('12x'))
    myassert([2,3],find_symbols('12xy1'))
    myassert([], find_symbols('467..114..'))

def test_find_stars():
    myassert([],find_stars(''))
    myassert([],find_stars('12+-/2'))
    myassert([0],find_stars('*'))
    myassert([2],find_stars('12*'))
    myassert([2,3],find_stars('12**1'))
    myassert([], find_stars('467..114..'))


test_find_numbers()
test_find_symbols()
test_find_stars()

#s = process(r'C:\py\github\aoc2023\3_.dat')
#myassert(4361, s)
#print(s)
s = process2(r'C:\py\github\aoc2023\3.dat')
print(s)