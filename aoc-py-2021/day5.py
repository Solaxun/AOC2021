import re
from collections import Counter
data = open('day5.txt').read()
nums = [int(x) for x in re.findall('\d+',data)]
segments = [nums[i:i+4] for i in range(0,len(nums),4)]

def is_horizontal(vec):
    x1,y1,x2,y2 = vec
    return x1 == x2

def is_vertical(vec):
    x1,y1,x2,y2 = vec
    return y1 == y2

def is_diagonal(vec):
    x1,y1,x2,y2 = vec
    return abs(x1-x2) == abs(y1-y2)

horizontal = [seg for seg in segments if is_horizontal(seg)]
vertical   = [seg for seg in segments if is_vertical(seg)]
diagonal   = [seg for seg in segments if is_diagonal(seg)]

def extend_horizontal(vector):    
    x1,y1,x2,y2 = vector
    miny,maxy = sorted([y1,y2])
    points = [(x1,y1),(x2,y2)]
    for y in range(miny+1,maxy):
        points.append(tuple([x1,y]))
    return tuple(points)

def extend_vertical(vector):    
    x1,y1,x2,y2 = vector
    minx,maxx = sorted([x1,x2])
    points = [(x1,y1),(x2,y2)]
    for x in range(minx+1,maxx):
        points.append(tuple([x,y1]))
    return tuple(points)

def extend_diagonal(vector):    
    x1,y1,x2,y2 = vector
    xdir = 1 if x2 > x1 else -1
    ydir = 1 if y2 > y1 else -1
    
    diags = [(x1,y1)]
    while x1 != x2:
        x1,y1 = x1+xdir, y1+ydir
        diags.append((x1,y1))
    return tuple(diags)

# print(extend_diagonal([0,5,4,1]))
# print(extend_diagonal([4,1,0,5]))

segments = []
for h in horizontal:
    segments.extend(extend_horizontal(h))
for v in vertical:
    segments.extend(extend_vertical(v))
for v in diagonal:
    segments.extend(extend_diagonal(v))

c = Counter(tuple(segments))
intersections = 0
for k,v in c.items():
    if v > 1:
        intersections += 1
print(intersections)