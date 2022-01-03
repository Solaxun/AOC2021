from functools import cache
import itertools

## day 21 part 1
player_state = {0:[7,0],1:[1,0]} # player:[position,score]

def mod1(num,m): return num % m or m
def die_range(start,end): return [mod1(n,100) for n in range(start,end)]

game_on = True
die = 1
dierolls = 0

while game_on:  
    for i in range(2):
        dierolls += 3
        roll = die_range(die,die+3)
        player = i % 2
        board_pos = player_state[player][0]
        new_pos = points = mod1(board_pos + sum(roll),10) 
        player_state[player][0] = new_pos
        player_state[player][1] += points
        curscore = player_state[player][1]  
        if curscore >= 1000:
            game_on = False
            print(dierolls * player_state[abs(player-1)][1])
            break
        die += 3

def mod1(num,m): return num % m or m

@cache
def play_round(player,pos1,score1,pos2,score2):
    if score1 >= 21:
        return 1,0
    if score2 >= 21:
        return 0,1
    wins1,wins2 = 0,0
    for roll in itertools.product([1,2,3],repeat=3):
        r = sum(roll)
        if player == 1:        
            new_pos = points = mod1(pos1 + r,10)
            w1,w2 = play_round(2,new_pos,score1+points,pos2,score2)
        else:
            new_pos = points = mod1(pos2 + r,10)
            w1,w2 = play_round(1,pos1,score1,new_pos,score2+points)
        wins2 += w2
        wins1 += w1
    return wins1,wins2

print(play_round(1,7,0,1,0))