from heapq import heappop,heappush
data = open('day15.txt').read().splitlines()

GRID = [list(map(int,list(d))) for d in data]
start = (0,0)
goal = len(data)-1,len(data[0])-1 

def in_bounds(grid,c):
    return c if 0 <= c[0] < len(grid) and 0 <= c[1] < len(grid[0]) else None

def neighbors(grid,c):
  nbors = [tuple(map(sum,zip(c,m))) for m in [[0,1],[1,0],[0,-1],[-1,0]]]
  return [n for n in nbors if in_bounds(grid,n)]

## part 2 setup
def one_mod(n): return (n-1) % 9 + 1

def expand_row(row,n=5):
    res = []
    for i in range(n):
        res.extend([one_mod(r + i) for r in row])
    return res

rows = []
for row in GRID:
    rows.append(expand_row(row))

cols = []
for col in zip(*rows):
    cols.append(expand_row(col))


GRID2 = zip(*cols)
goal2 = len(GRID2)-1,len(GRID2[0])-1
## end part 2 setup

def search(start,grid,goal,neighbors):
    frontier, seen = [(0, (0,0))], set((0,0))
    while frontier:
        cost, loc = heappop(frontier)
        if loc == goal: return cost
        for n in neighbors(loc):
            if n not in seen:
                seen.add(n)
                heappush(frontier,(cost + GRID2[n[0]][n[1]], n))

print(search((0,0),GRID,goal,lambda s: neighbors(GRID,s)))
print(search((0,0),GRID2,goal2,lambda s: neighbors(GRID2,s)))