import re

print(r'Processing...')
s = 0
lineno=0

with open(r'c:\py\github\aoc2023\2.dat') as f:
    while True:
        line = f.readline()
        if not line:
            break
        line = line.strip()
        lineno += 1
        print(lineno, line)
        games = re.split(': |; ', line)
#        print('games',games)
        games.pop(0)
        possible = True
        for g in games:
            d = {
            "red": 0,
            "green": 0,
            "blue": 0
            }
            cubes=re.split(', ',g)
            for c in cubes:
                info = re.split(' ',c)
                num = int(info[0])
                color = info[1]
                d[color] += num
            if d['red'] > 12 or d['green'] > 13 or d['blue'] > 14:
#                print(lineno,'impossible')
                possible = False
                break
        if (possible):
          s += lineno
        print(s)

print('finally: ',s)