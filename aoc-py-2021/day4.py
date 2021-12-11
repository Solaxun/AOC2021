import re

data = open('day4.txt').read().split('\n\n')
hand, *boards = data
boards = " ".join(boards)

hands  = [int(n) for n in hand.split(',')]
nums   = [int(n) for n in re.findall("(\d+)",boards)]
fives  = [nums[i:i+5] for i in range(0,len(nums),5)]
boards = [fives[i:i+5] for i in range(0,len(fives),5)]

def place_piece(piece,board):
    for r, row in enumerate(board):
        for n, num in enumerate(row):
            if piece == num:
                board[r][n] = '*'

def board_wins(board): 
    return rows_filled(board) or cols_filled(board)

def rows_filled(board):
    for row in board:
        if row.count('*') == 5:
            return True

def cols_filled(board):
    return rows_filled(zip(*board))

def get_unfilled(board):
    res = []
    for row in board:
        for num in row:
            if num != '*':
                res.append(num)
    return res

def score(board,latest_called_num):
    open = get_unfilled(board)
    summed = sum(open)
    return summed * latest_called_num

def bingo(first_winner=True):
    scores,winners_ixs = [],set()
    while hands:
        h = hands.pop(0)
        for i,board in enumerate(boards):
            place_piece(h,board)
            if board_wins(board):
                s = score(board,h)
                if first_winner:
                    return s
                if i not in winners_ixs: # already won prior round
                    scores.append(s)
                    winners_ixs.add(i)
    return scores[-1]

# each of these mutates both hands and boards - so to remove the influence of 
# one on the other, comment the other out while running one of the below.  It 
# actually returns the correct answer even without doing so because in the 2nd
# problem we want the last winner, so it picks up where the first problem left
# off, e.g. we don't stop until the last board wins, so if we have the first 
# board already marked and the board mutated up until the first win, it's fine
# because we would have done the same thing in the second problem up until the
# final winner.  Note that if we switched the order of the functions running 
# below this would not work.  We can make them completely independent if desired
# by making a copy of boards and hand to each input.
print(bingo(first_winner=True))
print(bingo(first_winner=False))
