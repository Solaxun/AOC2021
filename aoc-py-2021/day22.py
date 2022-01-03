import re

data = open('day22.txt').read()

# easier than parsing coords b/w -50/+50 (first 20 of input data are
# in this range)
below50 = data.splitlines()[0:20]

## part 1
on = set()
for line in below50:
    x1,x2,y1,y2,z1,z2 = [int(x) for x in re.findall('-?\d+',line)]
    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            for z in range(z1,z2+1):
                if line.startswith('on'):
                    on.add((x,y,z))
                else:
                    on.discard((x,y,z))

print(len(on))

## part 2... rutroh
import re
data = open('day22.txt').read()

def build_cube(x1,x2,y1,y2,z1,z2):
  coords = set()
  for x in range(x1,x2+1):
    for y in range(y1,y2+1):
      for z in range(z1,z2+1):
        coords.add((x,y,z))
  return coords,len(coords)

on_coords = []
off_coords = []
for line in data.splitlines():
  parsed = [int(x) for x in re.findall('-?\d+',line)]
  if line.startswith('on'):
    on_coords.append(parsed)
  else:
    off_coords.append(parsed)

(x1,x2,y1,y2,z1,z2),*ons = on_coords
for X1,X2,Y1,Y2,Z1,Z2 in ons:
  x1 = min(x1,X1)
  x2 = max(x2,X2)
  y1 = min(y1,Y1)
  y2 = max(y2,Y2)
  z1 = min(z1,Z1)
  z2 = max(z2,Z2)
print(x1,x2,y1,y2,z1,z2)
print(build_cube(x1,x2,y1,y2,z1,z2))