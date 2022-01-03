data = [list(x) for x in open('day25.txt').read().splitlines()]

def find_open(coll,dir='>'):
    movers = []
    for i,x in enumerate(coll):
        if x == '.' and coll[i-1] == dir:
            movers.append(i-1)
    return movers

def move(coll,dir='>'):
    coll = list(coll)
    movers = find_open(coll,dir)
    if movers:
        for loc in movers:
            coll[loc] = '.'
            coll[(loc+1) % len(coll)] = dir
    return "".join(coll)

def step(cucumbers):
    cucumbers = [move(c,dir='>') for c in cucumbers]
    cucumbers = [move(c,dir='v') for c in zip(*cucumbers)]
    return list(zip(*cucumbers))

def part1():
    cucumbers = data
    i = 1
    while True:
        cs = step(cucumbers)
        if cucumbers == cs:
            return i
        i += 1
        cucumbers = cs

assert move('>..>') == '.>.>'
assert move('>.>') == '.>>'
assert move('>>.') == '>.>'
assert move('>>..>.') == '>.>..>'

# ele = '.>.>'
# # .>..
# # .>.> | >..>
# # y = [b if b == '>' and a == '.' else b for a,b in zip(x,x[-1]+x[1:])]
# res = []
# for i,x in enumerate(ele):
#     if ele[i-1] == '>' and x == '.':
#         res.append('>')
#     else:
#         res.append(ele[i-1])
# print(res)