data = open('day20.txt').read()
enhancements,image = data.split('\n\n')
image = image.splitlines()
enhancements = "".join(enhancements.splitlines())

def neighbor_locs(x,y):
    # includes original position x,y
    return [(x+x1, y+y1) for x1 in [-1,0,1] for y1 in [-1,0,1]]

def grid(image):
    return {(r,c):pixel 
            for r,row in enumerate(image) 
            for c,pixel in enumerate(row)}

def neighbors_to_enh(grid,neighbors,iter=0):
    default = '.' if iter % 2 == 0 else '#'
    neighbors = ''.join(grid.get(loc,default) for loc in neighbors)
    binstr = ''.join('1' if n == '#' else '0' for n in neighbors)
    return enhancements[int(binstr,2)]

def enhance(grid,iter=0):
    new_grid, neighbors = {}, set()
    for coord in grid:
        ns = neighbor_locs(*coord)
        enh = neighbors_to_enh(grid,ns,iter)
        neighbors |= set(ns)
        new_grid[coord] = enh
  
    for coord in neighbors:
        ns = neighbor_locs(*coord)
        enh = neighbors_to_enh(grid,ns,iter)
        new_grid[coord] = enh
    return new_grid 

# very slow for part 2 with 50 iters... consider more efficient way
# to handle neighbors of neighbors to avoid redundant checks
def simulate(image,n):    
    for i in range(n):
        image = enhance(image,i)
    print(len([pixel for pixel in image.values() if pixel == '#']))

image = grid(image)

simulate(image,2)
simulate(image,50)