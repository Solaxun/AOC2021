start = 0,0
xmin,xmax,ymin,ymax = 94,151,-156,-103 # hardcode input

def target_reached(x,y): 
    return xmin <= x <= xmax and ymin <= y <= ymax

def target_passed(x,y):
     return x > xmax or y < ymin

def step(x,y,xv,yv):
    xvadj = -1 if xv > 0 else 1 if xv < 0 else 0
    return (x + xv, y + yv, xv + xvadj, yv -1)

def launch_probe(x,y,xv,yv):
    apex = -float('inf') 
    while not target_passed(x,y):
        x,y,xv,yv = step(x,y,xv,yv)
        if y > apex:
            apex = y
        if target_reached(x,y):
            return apex

highest = set()
velocities = set()
for xv in range(-160,160):
    for yv in range(-160,160):
        apex = launch_probe(*start,xv,yv)
        if apex is not None:
            highest.add(apex)
            velocities.add((xv,yv))
    
print(max(highest))
print(len(velocities))