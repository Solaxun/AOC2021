data = open('day11.txt').read().splitlines()
nums = [list(map(int,line)) for line in data]

def in_bounds(loc): 
    return 0 <= loc[0] < len(nums) and 0 <= loc[1] < len(nums[0])

def neighbor_locs(loc):
    moves = [(r,c) for r in [0,1,-1] for c in [0,1,-1] if not (r,c) == (0,0)]
    return tuple(tuple(map(lambda x,y:x+y,m,loc)) for m in moves)

def incr_by_one(octopi):
    return  [list(map(lambda x: x+1,row)) for row in octopi]

def none_will_flash(octopi,flashed_locs):
    return all((r,c) in flashed_locs or col <= 9
              for r,row in enumerate(octopi) 
              for c,col in enumerate(row))

def reset_flashed(octopi,flashed_locs):
    return [[col if (r,c) not in flashed_locs else 0 
             for c,col in enumerate(row)]
             for r,row in enumerate(octopi)]
    
def flash(octopi,flashed_locs=set(),nflashed=0):
    if none_will_flash(octopi,flashed_locs):
        return [reset_flashed(octopi,flashed_locs),nflashed]
    flashed = set()
    for i,row in enumerate(octopi):
        for j,col in enumerate(row):
            if col > 9 and not (i,j) in flashed_locs:
                flashed.add((i,j))
                nlocs = tuple(n for n in neighbor_locs([i,j]) if in_bounds(n))
                
                for r,c in nlocs:
                    octopi[r][c] += 1                    
    return flash(octopi,flashed_locs.union(flashed),nflashed+len(flashed))

def step(octopi):
    return flash(incr_by_one(octopi))

# part 1
octopi,flashed = nums,0
for i in range(100):
    octopi,flashes = step(octopi)
    flashed += flashes 
print(flashed)

# part 2
i = 0
octopi = nums
while 1:
    octopi,flashes = step(octopi)
    i += 1
    if flashes == 100:
        break
print(i)