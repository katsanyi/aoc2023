import re
import copy
import sys

print(r'Processing...')

seeds = []
input = []
output = []
location = []

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



def processfirstline(line):
    parts = re.split(' ', line)
    parts.pop(0)
    return [int(x) for x in parts]

def processfirstline2(line):
    parts = re.split(' ', line)
    parts.pop(0)
    ret = []
    while len(parts) > 0:
        start = int(parts.pop(0))
        range = int(parts.pop(0))
        ret.append((start,start + range - 1))
    return ret


def processline(line):
    parts = re.split(' ', line)
    return [int(x) for x in parts]

def processline2(line):
    parts = re.split(' ', line)
    return (int(parts[1]),int(parts[1]) + int(parts[2]) - 1, int(parts[0]) - int(parts[1]))
#    return [int(x) for x in parts]


#assumption: file is not empty
def read(fname):
    global location
    location = []
    global input
    input = []
    fc = readfile(fname)
    global seeds
    seeds = processfirstline(fc[0])
    fc.pop(0)
    fc.pop(0)
    fc.pop(0)
    fc.append('') # make sure the list ends in an empty line to finish processing of last bucket
    i = 0 # index of line being processed
    j = 0 # index of bucket being processed, seed-to-soil map = 0
    map = []
    while i < len(fc):
        if '' == fc[i]:
            input.append(map)
            map = []
        elif ':' in fc[i]:
            j += 1
        else:
            map.append(processline(fc[i]))
        i += 1
'''
Input: fname
Outputs:
  global seeds: 
  global input: 
'''
def read2(fname):
    global location
    location = []
    global input
    input = []
    fc = readfile(fname)
    global seeds
    seeds = processfirstline2(fc[0])
    fc.pop(0)
    fc.pop(0)
    fc.pop(0)
    fc.append('') # make sure the list ends in an empty line to finish processing of last bucket
    i = 0 # index of line being processed
    j = 0 # index of bucket being processed, seed-to-soil map = 0
    map = []
    while i < len(fc):
        if '' == fc[i]:
            input.append(map)
            map = []
        elif ':' in fc[i]:
            j += 1
        else:
            map.append(processline2(fc[i]))
        i += 1

def process0():
    for i in seeds:
        mappedi = i
        for j in input:
            for k in j:
                if k[1] <= mappedi <= k[1] + k[2] - 1:
                    x = k[0] + mappedi - k[1]
                    mappedi = x
                    break
        location.append(mappedi)

def process():
    global output
    global location
    output = [seeds]
    for i in range(len(input)): # let's iterate through all the levels
        o =[]
        for j in output[i]: # items to map
            mapped = j
            for k in input[i]: # maps
                if k[1] <= j <= k[1] + k[2] - 1:
                    x = k[0] + j - k[1]
                    mapped = x
                    break
            o.append(mapped)
        output.append(o)
    location = output[-1]

#returns True if closed intervals [s1,e1] and [s2,e2] are intersecting
def is_interstecting(i1,i2):
    return not (i1[0] > i2[1] or i1[1] < i2[0])
#    return not (s1 > e2 or e1 < s2)

def test_is_interstecting():
    myassert(True,is_interstecting((1,2),(1,2)))
    myassert(True,is_interstecting((1,2),(1,3)))
    myassert(True,is_interstecting((1,2),(0,2)))
    myassert(True,is_interstecting((1,2),(0,20)))
    myassert(True,is_interstecting((1,2),(0,1)))
    myassert(False,is_interstecting((10,20),(0,1)))
    myassert(False,is_interstecting((10,20),(30,31)))

test_is_interstecting()
#sys.exit(0)

# returns the disjoint intervals covering the first interval, as it is cut by the 2nd interval
# it does not return any potential parts of the 2nd interval that is before or after the 1st one
# assumption: the intervals are intersecting
def interval_cuts0(s1,e1,s2,e2):
    a = []
    # cases     1    2       3      4
    #          ###  ####    ###     ##
    #           ###  ##    ##     #####
    # results
    #          #    #       #       ##
    #           ##   ##      ##
    #                  #
    if   s1 < s2 <= e1 <= e2: #1
        a = [(s1,s2-1),(s2,e1)] # 2nd is covered
    elif s1 < s2 <= e2 < e1: #2
        a = [(s1,s2-1),(s2,e2),(e2+1,e1)] # 2nd is covered
    elif s2 <= s1 <= e2 < e1: #3
        a = [(s1,e2),(e2+1,e1)] # 1st is covered
    elif s2 <= s1 <= e1 <= e2: #4
        a = [(s1,e1)] #  covered
    else:
        print('Non-intersecting? !!!!!')
    #seriously incomplete
    #overly complicated
    # getting the < / <= right seems dounting
    #goal would be also to know which intervals are overlapping
    '''
    consider these points:
    s1, e1, if s1 between s1 and e1 then s1, if e2 between s1 and e1 then e2 
    '''
    return a

# input: start of iv1, end, etc.
def interval_cuts(s1,e1,s2,e2):
    if not is_interstecting((s1,e1),(s2,e2)):
        return [(s1,e1)],[],[(s2,e2)]
    only1 = []
    only2 = []
    common = []
    # cases     1    2       3      4
    #          ###  ####    ###     ##
    #           ###  ##    ##     #####
    # results
    #          #    #       #       ##
    #           ##   ##      ##
    #                  #
    if   s1 < s2 <= e1 <= e2: #1
        only1 = [(s1,s2-1)]
        common = [(s2,e1)]
        if e2 > e1:
          only2 = [(e1+1,e2)]
        else:
          only2 = []
    elif s1 < s2 <= e2 < e1: #2
        only1 = [(s1,s2-1),(e2+1,e1)]
        common = [(s2,e2)]
        only2 = []
    elif s2 <= s1 <= e2 < e1: #3
        only1 = [(e2+1,e1)]
        common = [(s1,e2)]
        if s2 < s1:
          only2 = [(s2,s1-1)]
        else:
          only2 = []
    elif s2 <= s1 <= e1 <= e2: #4
        only1 = []
        common = [(s1,e1)]
        only2 = []
        if s2 < s1:
          only2.append((s2,s1-1))
        if e1 < e2:
          only2.append((e1+1,e2))
    else:
        print('Non-intersecting? !!!!!')
#    print('only1', only1)
#    print('only2', only2)
#    print('common', common)
    s = 0
    for ii in [only1, common, common, only2]:
        for i in ii:
            if i[0] > i[1]:
                print('Not cool at all')
            s = s + i[1] - i[0] + 1
    if s != e1-s1 +1 + e2-s2+1:
        print('Again, not cool')
        print('ivs:',e1,s1,e2,s2)
        print('s:',s)
        print(e1-s1 +1 + e2-s2+1)
        print(s1,e1,s2,e2)
        sys.exit(-1)
    return only1, common, only2


def test_interval_cuts():
  #print('test_interval_cuts()')
  myassert(([(4, 4)], [(5, 6)], [(7, 7)]),interval_cuts(4,6,5,7)) # clear 1
  myassert(([(4, 4)], [(5, 6)], []),interval_cuts(4, 6, 5, 6))
  myassert(([(1, 1), (4, 4)], [(2, 3)], []),interval_cuts(1,4,2,3)) # clear 2
  myassert(([(6, 6)], [(4, 5)], [(1, 3)]),interval_cuts(4,6,1,5)) # clear 3
  myassert(([], [(4, 6)], [(1, 3), (7, 7)]),interval_cuts(4,6,1,7)) # clear 4
  myassert(([], [(1, 4)], []),interval_cuts(1, 4, 1, 4))
  myassert(([], [(1, 1)], []),interval_cuts(1, 1, 1, 1))
  myassert(([], [(1, 1)], [(0, 0)]),interval_cuts(1, 1, 0, 1))
  myassert(([(2, 2)], [(1, 1)], [(0, 0)]),interval_cuts(1, 2, 0, 1))
  myassert(([], [(1, 1)], [(2, 2)]),interval_cuts(1, 1, 1, 2))
  myassert(([(1, 1)], [], [(2, 2)]),interval_cuts(1, 1, 2, 2))
  myassert(([(97, 98)], [(93, 96)], []),interval_cuts(93, 98, 93, 96))

test_interval_cuts()
#sys.exit(0)

# input: 2 lists of intervals (tuples: (start,stop, optional extras) )
# 1st is the interval to cut
# 2nd is what determines cutting
# output is also a list of intervals
# requirement: union of return is the same as source
# each interval in the reurn list is either fully included in every cutting iv, or fully disjoint
def intervals_cut(source,cutter):
    ivset = copy.deepcopy(source)
    for i in cutter:
        newset = []
        for j in ivset:
            only1, common, only2 = interval_cuts(j[0],j[1],i[0],i[1])
            newset.extend(only1)
            newset.extend(common)
        ivset = newset
    return ivset

def test_intervals_cut():
    myassert([(4,6)],intervals_cut([(4,6)],[]))                     # empty cutter
    myassert([(4,6)],intervals_cut([(4,6)],[(7,8,3)]))                # disjoint cutter
    myassert([(4,5),(6,6)],intervals_cut([(4,6)],[(6,8,'qqq')]))          # cut at the very end
    myassert([(4,5),(6,6)],intervals_cut([(4,6)],[(6,8),(7,8)]))    # one cuts, one disjoint
    myassert([(1,2),(4,6)],intervals_cut([(1,2),(4,6)],[(7,8)]))    # 2 ivs in input, cutters like above
    myassert([(1,2),(4,5),(6,6)],intervals_cut([(1,2),(4,6)],[(6,8)]))
    myassert([(1,2),(4,5),(6,6)],intervals_cut([(1,2),(4,6)],[(6,8),(7,8)]))
    myassert([(1,2),(4,5),(6,6)],intervals_cut([(1,2),(4,6)],[(6,8),(7,8),(0,3)])) # additional cutter, not in order
    myassert([(1,2),(4,5),(6,6)],intervals_cut([(1,2),(4,6)],[(6,8),(7,8),(0,2)]))
    myassert([(2,2),(1,1),(4,5),(6,6)],intervals_cut([(1,2),(4,6)],[(6,8),(7,8),(0,1)]))
    myassert([(2,2),(1,1),(4,5),(6,6)],intervals_cut([(1,2),(4,6)],[(6,8),(7,8),(0,1),(0,1)])) # dupes in cuter

# source and shifter are list of tuples like in intervals_cut
# assumption is that sifter does not cut source (i.e. intervals_cut was run before)
# shifts source intervals by shifts (3rd value) of including ivs in shifter
def intervals_shift(source,shifter):
    ret = []
    for i in source:
        ii = i
        for j in shifter:
            if is_interstecting(i,j):
                ii=(i[0]+j[2],i[1]+j[2])
                break
        ret.append(ii)
    return ret

def test_intervals_shift():
    myassert([(2,3)],intervals_shift([(2,3)],[]))           # empty shifter
    myassert([(2,3)],intervals_shift([(2,3)],[(4,5,6)]))    # disjoint shifter
    myassert([(8,9)],intervals_shift([(2,3)],[(1,5,6)]))    # single shifter
    myassert([(1,2)],intervals_shift([(2,3)],[(1,5,-1)]))   # negative shifter
    myassert([(8,9)],intervals_shift([(2,3)],[(1,5,6),(9,9,9)]))    # multiple shifters
    myassert([(7,7),(8,9),(18,18)],intervals_shift([(1,1),(2,3),(9,9)],[(1,5,6),(9,9,9)]))    # multiplesource and shifters
    myassert([(2,3)],intervals_shift([(2,3)],[]))           # empty shifter

test_intervals_shift()
#sys.exit(0)

def iv_cut(iv,n):
    if iv[0] < n < iv[1]:
        ret = [(iv[0],n),(iv[1])]

def test_iv_cut():
    myassert([(4,6)],iv_cut((4,6),1))

#test_iv_cut()
test_intervals_cut()
#sys.exit((0))

#test_interval_cuts()
#sys.exit(-1)
#print('-----')

'''
Plan 
  handle non-intersecting + above 4 cases
  output[i+1] is going to be the mapping of 1-2-3 intervals as split from output[i]
  Since the mappings are not disjoint, we need to be careful
'''



def process2():
    global output # list of tuples with intervals
    global location
    output = [seeds]
#    print('input:',input)
    for i in range(len(input)): # let's iterate through all the levels
        o =[]
#       print('input-:', input)
        print('output-:', output)
        print('output[i]:', output[i])
        for j in output[i]: # items to map
#            print('j::', j)
            for k in input[i]: # maps
#                print('k::', k)
                # input iv: j[0] --- j[0] + j[1] - 1
                # mapping from iv k[1] --- k[1] + k[2] - 1:
                shift = k[0] - k[1]
                only1, common, only2 = interval_cuts(j[0], j[1], k[1], k[1] + k[2] - 1)
                if only1:
                  o.extend(only1)
                for l in common:
                    o.append((l[0]+shift,l[1]+shift))
#                    break
#            o.append(mapped)
        output.append(o)
    location = output[-1]

'''
Proceed level by level
first cut intervals to map so that they are either disjoint or included in each mapper
then apply shift
start next level with this as input
'''
def process3():
    global output # list of tuples with intervals
    global location
    ivset0 = seeds
#    print('input:',input)
    for i in input: # let's iterate through all the levels
#   for i in range(len(input)):  # let's iterate through all the levels
        print('i:',i)
        ivset1 = intervals_cut(ivset0,i)
        print('ivset1:',ivset1)
        ivset0 = intervals_shift(ivset1, i)
        print('ivset0:',ivset0)
    return ivset0





def score1():
    l = copy.deepcopy(location)
    l.sort()
    return l[0]

def score2(location):
    m = location[0][0]
    for i in location:
      if i[0] < m:
          m = i[0]
    return m


def test_processfirstline():
    myassert([79,14,55,13],processfirstline('seeds: 79 14 55 13'))

def test_processfirstline2():
#    myassert([(79, 14), (55, 13)],processfirstline2('seeds: 79 14 55 13'))
    myassert([(79, 92), (55, 67)],processfirstline2('seeds: 79 14 55 13'))

test_processfirstline()
test_processfirstline2()
test_is_interstecting()


read(r'C:\py\github\aoc2023\5_.dat')
process()
s = score1()
#print('test for 1',s)
myassert(35, s)

read(r'C:\py\github\aoc2023\5.dat')
process()
s = score1()
#print('Real 1',s)
myassert(324724204, s)

print('going ahead for 2')

read2(r'C:\py\github\aoc2023\5_.dat')
print('seed:', seeds)
print('input', input)
location = process3()
print('location: ',location)
#add_inputs()
s = score2(location)
print('test for 2',s)
myassert(46, s)

read2(r'C:\py\github\aoc2023\5.dat')
print('seed:', seeds)
print('input', input)
location = process3()
print('location: ',location)
#add_inputs()
s = score2(location)
print('test for 2',s)
myassert(46, s)





#s = score2()
#print(s)