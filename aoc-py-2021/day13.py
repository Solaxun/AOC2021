import re
data = open('day13.txt').read()
coords = [(int(x),int(y)) for x,y in re.findall('(\d+),(\d+)',data)]
splits = [(ax,int(amt))for ax,amt in re.findall('([xy])=(\d+)',data)]

def fold_coord(coord,axis,split_ix):
  x,y = coord
  if axis == 'x':
    return (x - 2 * (x - split_ix), y) if x - split_ix > 0 else (x,y)    
  return (x, y - 2 * (y - split_ix)) if y - split_ix > 0 else (x,y)

for i,(axis,split_ix) in enumerate(splits):
  coords = set(fold_coord(c,axis,split_ix) for c in coords)
  if i == 0:print(len(set(coords))) # part 1

def display(coords):
  maxx,maxy = max(x for x,y in coords), max(y for x,y in coords)
  empty = [[' ' for col in range(maxx+1)] for rows in range(maxy+1)]
  for x,y in coords:
    empty[y][x] = '#'
  for p in empty:print("".join(p))

display(coords)