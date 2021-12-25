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