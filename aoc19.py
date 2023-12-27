import re
import copy

class rule:
    def __init__(self, s):
        cond = ''
        if '<' in s: cond = '<'
        if '=' in s: cond = '='
        if '>' in s: cond = '>'
        if cond == '':
            self.set(False, None, None, None, s)
        else:
            l = re.split(('<|>|=|:'),s)
            self.set(True, l[0], cond, l[1], l[2])

    # result is either A/R or a rule
    def set(self, has_condition, variable, relation, value, result):
        self.has_condition = has_condition
        self.variable = variable
        self.relation = relation
        self.value = int(value) if value != None else None
        self.result = result

    def __str__(self):
        if self.has_condition:
            ret = f"{self.variable}{self.relation}{self.value}:{self.result}"
        else:
            ret = self.result
        return ret

class ruleset:
    name = ''   # name of the ruleset
    rules = []  # list of rules
    def __init__(self, s):
        l = re.split(('\{|\}'),s)
        self.name = l[0]
        rl = l[1].split(',')
        self.rules = []
        for i in rl:
            r = rule(i)
            self.rules.append(r)

    def __str__(self):
        ret = self.name + '{'
        first = True
        for i in self.rules:
            if first:
                first = False
            else:
                ret += ','
            ret += str(i)
        ret += '}'
        return ret

class part:
    def __init__(self, s):
        l = re.split(('\{|\}'),s)
        ll = re.split('x|m|a|s|,|=',l[1])
        self.variables = {}
        self.variables['x'] = int(ll[2])
        self.variables['m'] = int(ll[5])
        self.variables['a'] = int(ll[8])
        self.variables['s'] = int(ll[11])

    def score(self):
        return self.variables['x'] + self.variables['m'] + self.variables['a'] + self.variables['s']

    def get(self, var):
        return self.variables[var]

    def __str__(self):
        ret = f"{{x={self.variables['x']},m={self.variables['m']},a={self.variables['a']},s={self.variables['s']}}}"
        return ret

def readfile(fname):
    s=[]
    with open(fname) as f:
        while True:
            line = f.readline()
            if not line:
                break
            s.append(line.strip())
    return s

# returns:
# rulesets, dict mapping rule names to list of rules
def read(sl):
    firstpart = True
    rulesets = {}
    parts = []
    for i in sl:
        if i == '':
            firstpart = False
            continue
        if firstpart:
            rs = ruleset(i)
            #rulesets.append(rs)
            rulesets[rs.name] = rs
        else:
            p = part(i)
            parts.append(p)
    return rulesets, parts

# Returns A, R or the ruleset name to check next
def evaluate_ruleset(rset: ruleset, p: part):
    for i in rset.rules:
        if not i.has_condition:
            return i.result
        if i.relation == '<' and p.get(i.variable)  < i.value: return i.result
        if i.relation == '=' and p.get(i.variable) == i.value: return i.result
        if i.relation == '>' and p.get(i.variable)  > i.value: return i.result
    assert False
    return ''


def xxprocess_part(rulesets, part):
    current_rule = 'in'
    while current_rule not in 'AR':
        pass
    return current_rule

def process1part(rsets, p: part):
    current_name = 'in'
    while current_name not in 'AR':
        current_name = evaluate_ruleset(rsets[current_name], p)
    return current_name

def process(rulesets, parts):
    s = 0
    for i in parts:
        if process1part(rulesets,i) == 'A':
            s += i.score()
    return s

# this proves that there are no loops in the graph
def reachable(rsets):
    reachablel = ['in']
    to_process = ['in']
    while len(to_process) > 0:
        being_processed = to_process[-1]
        to_process.pop()
        #print('rsets[to_process]', rsets[being_processed])
        for i in rsets[being_processed].rules:
            res = i.result
            if res not in 'AR':
                assert res not in reachablel
                reachablel.append(res)
                to_process.append(res)
    #print(reachablel)
    return reachablel

def gen_paths(rsets):
    paths = [('in',[])]
    rp = []                                                                 #rule path
    to_process = [('in','in',[])]                                              # list of tuples, first is chain, 2nd is last
    print()
    print('rsets', rsets)
    while len(to_process) > 0:
        being_processed = to_process[-1]                                    # being processed is a chain of names
        to_process.pop()
        print('being_processed', being_processed)
        print('being_processed1', being_processed[1])
        print('rsets being_processed1', rsets[being_processed[1]])
        # being_processed[0] is the chain so far
        # being_processed[1] is the name of the last visited ruleset
        # rsets[being_processed[1]] is the last visited ruleset
        # rsets[being_processed[1]].rules is the list of rules in the last visited ruleset
        # i is one rule in that list
        # i.result is either A/R or the name of the next ruleset to process
        for i in rsets[being_processed[1]].rules:
            res = i.result
            newlistchain = copy.deepcopy(being_processed[2])
            newlistchain.append((i))
            if res not in 'AR':
                to_process.append((being_processed[0] + '-' + res, res, newlistchain))
            paths.append((being_processed[0] + '-' + res, newlistchain))

            rp.append([being_processed[0]])
            #+ '-' + res)
    print(paths)
    print(rp)
    accepted_paths = []
    x = []  # x[i] = 1 mean that
    m = []
    a = []
    s = []
    for i in range(4001):
        x.append(1)
        m.append(1)
        a.append(1)
        s.append(1)
    for i in paths:
        if i[0][-1] == 'A':
            accepted_paths.append(i)
    for i in accepted_paths:
        mins = {  # minimum of < rules for each letter
            'x': 4000,
            'm': 4000,
            'a': 4000,
            's': 4000,
        }
        maxs = {  # maximum of # rules for each letter
            'x': 0,
            'm': 0,
            'a': 0,
            's': 0,
        }
        print('i',i)
        for j in i[1]:
            if j.has_condition:
                print(str(j))
                if j.relation == '=':
                    mins[j.variable] = min(mins[j.variable], j.value - 1)
                    maxs[j.variable] = max(maxs[j.variable], j.value + 1)
                    mins[j.variable] = min(mins[j.variable], j.value - 1)
                else:
                    maxs[j.variable] = max(maxs[j.variable], j.value + 1)
        print('mins', mins)
        print('maxs', maxs)
'''
    It's cool that we have the accepting intervals for each path.
    How do we combine them though?
    We'd need to calculate volume of n 4-dimensional cubes, making sure that intersecting spaces are only counted once.
    Looks pretty hard! 
'''

    print('accepted_path', len(accepted_paths), accepted_paths)

    return paths