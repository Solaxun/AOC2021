data = open('day2.txt').read().splitlines()

depth, horizontal = 0,0
for line in data:
    dir,amt = line.split()
    amt = int(amt)
    if dir == 'forward':
        horizontal += amt
    elif dir == 'down':
        depth += amt
    elif dir == 'up':
        depth -= amt

print(depth * horizontal)

depth, horizontal, aim = 0,0,0
for line in data:
    dir,amt = line.split()
    amt = int(amt)
    if dir == 'forward':
        horizontal += amt
        depth = depth + aim * amt
    elif dir == 'down':
        aim += amt
    elif dir == 'up':
        aim -= amt

print(depth * horizontal)