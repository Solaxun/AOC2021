data = open('day9.txt').read().splitlines()
data = [list(map(int,list(line))) for line in data]

def in_bounds(loc):
    return 0 <= loc[0] < len(data) and 0 <= loc[1] < len(data[0])

def neighbor_locs(loc):
    moves = [[-1,0],[0,-1],[1,0],[0,1]]
    return tuple(tuple(map(lambda x,y:x+y,m,loc)) for m in moves)

def lowest_adjacent(row,col):
    nlocs = [n for n in neighbor_locs((row,col)) if in_bounds(n)]
    neighbor_nums = [data[r][c] for r,c in nlocs]
    if min(neighbor_nums) > data[row][col]:
        return True

risk_level = []
lowest_locs = []
for r,row in enumerate(data):
    for c,col in enumerate(row):
        if lowest_adjacent(r,c):
            lowest_locs.append((r,c)) # for part 2
            risk_level.append(col+1)
    
print(sum(risk_level))

## part 2
def expand_basin(loc):
    locs = [loc]
    visited = set()
    basin = {loc}
    while locs:
        r,c = loc = locs.pop()
        # don't go back to where we came from
        visited.add(loc)
        nlocs = [n for n in neighbor_locs(loc) if not n in visited and in_bounds(n)]
        for r1,c1 in nlocs:
        # neighbor is bigger than where we came from, e.g. uphill (ignoring 9's)
            if data[r1][c1] > data[r][c] and data[r1][c1] != 9:
                locs.append((r1,c1))
                basin.add((r1,c1))
    return len(basin)

basins = sorted((expand_basin(lowest) for lowest in lowest_locs),reverse=True)
score = 1
for b in basins[0:3]:
    score *= b
print(score)
