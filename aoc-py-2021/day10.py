data = open('day10.txt').read().splitlines()
closing = {'}':'{',']':'[','>':'<',')':'('}

def check_line(line):
    matching = []
    for l in line:
        if l in closing:
            opened = matching.pop()
            if closing[l] != opened:
                return l
        else:
            matching.append(l)

points = {')':3,']':57,'}':1197,'>':25137}

print(sum(points.get(check_line(line)) for line in data if check_line(line)))

def incomplete_line(line):
    matching = []
    for l in line:
        if l in closing:
            opened = matching.pop()
            if closing[l] != opened:
                return False
        else:
            matching.append(l)
    return matching

incomplete = []
for line in data:
    ic = incomplete_line(line)
    if ic:
        incomplete.append(ic)

def score(completion):
    s = 0
    pts = {'(':1,'[':2,'{':3,'<':4}
    # reverse to start from end - most recent opening bracket unmatched
    completion = reversed(completion)
    for c in completion:
        s = 5 * s + pts[c] 
    return s

def middle(coll):
    return coll[len(coll)//2]

print(middle(sorted(score(ic) for ic in incomplete)))