from collections import defaultdict

data = open('day12.txt').read().splitlines()
lkp = defaultdict(list)

for line in data:
    a,b = line.split('-')
    lkp[a].append(b)
    lkp[b].append(a)

def no_small_dups(path):
    lower = [p for p in path if p.islower()]
    unique = set(lower)
    return len(lower) -1 <= len(unique)
            
paths = [['start']]
all_paths = set()
while paths:
    path = paths.pop()
    cave = path[-1]
    if cave == 'end':
        all_paths.add(tuple(path))
        continue
    neighbors = lkp[cave]
    for n in neighbors:
        # or n not in path for part 1
        if n.isupper() or no_small_dups(path) and n != 'start':
            paths.append(path + [n])
    
print(len(all_paths))
# print(has_small_dups(['fred','bob','sue','fred' ,'sue']))