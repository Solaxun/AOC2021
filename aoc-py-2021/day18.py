import re
import math

data = open('day18.txt').read()

def depth4_range(fish):
    depth = 0
    for ix,x in enumerate(fish):
        # print(ix,x,depth)
        if x == '[':
            depth += 1
        if x == ']':
            depth -=1
        # first bracket is zero, so 5 is really depth 4
        if depth == 5 and x == '[':
            if fish[ix+1] == '[':
                continue
            start = ix
            end = fish.find(']',ix)
            return start,end #+1
    return None, None

def right_neighbor(fish,ix):
    # return beg and end index of number
    while not fish[ix].isnumeric() and ix < len(fish)-1:
        ix +=1
    start = end = ix
    while fish[end].isnumeric():
        end += 1
    # no number to right found
    if start == end and fish[end] == ']':
        return None,None
    return start,end    

def left_neighbor(fish,ix):
    while not fish[ix].isnumeric() and ix > 0:
        ix -=1
    start = end = ix
    while fish[start].isnumeric() and not fish[start] == '[':
        start -= 1
    # no number to left found
    if start == end and fish[start] == '[':
        return None,None
    return start+1,end+1

def explode(fish):
    # start/end index of brackets at depth 4
    start,end = depth4_range(fish)
    # nothing of depth 4 found, no change
    if start is None:
        return fish
    # numbers begin one index past starting bracket
    startend = start + 1 
    while fish[startend].isnumeric():
        startend += 1
    # numbers end one index before ending bracket 
    begend = end - 1
    while fish[begend].isnumeric():
        begend -= 1
 
    # find first number that is to left and right of this, if any
    rbeg,rend = right_neighbor(fish,end)
    lbeg,lend = left_neighbor(fish,start)

    if rbeg is not None:
        fish = fish[0:rbeg] + str(int(fish[rbeg:rend]) + int(fish[begend+1:end])) + fish[rend:]
    if lbeg is not None:
        fish = fish[0:lbeg] + str(int(fish[lbeg:lend]) + int(fish[start+1:startend]))  + fish[lend:]
    # recalculate start/end brackets because adding digits e..g 9->10
    # may increase str length and change the start/end indices
    start,end = depth4_range(fish)
    fish = fish[0:start] + '0' + fish[end+1:]
    return fish

def split(fish):
    # first num >= 10
    tenplus = re.search('(\d{2,4})',fish)
    if tenplus is None:
        return fish
    tenplus = int(tenplus.group(0))
    # replace it with a pair, only the first occurrence is replaced
    repl = '[{},{}]'.format(tenplus//2,math.ceil(tenplus/2))
    return re.sub('\d{2,4}',repl,fish,1)

def add(s1,s2):
    sn = '[{},{}]'.format(s1,s2)
    while True:
        e = explode(sn)
        if e == sn:
            s = split(e)
            if s == e:
                return s
            else:
                sn = s
        else:
            sn = e

def add_all(nums):
    start,*nums = nums
    for num in nums:
        start = add(start,num) 
    return start    

def magnitude(sn):
    left,right = sn
    if isinstance(left,list):
        left = magnitude(left)
    if isinstance(right,list):
        right = magnitude(right)
    return 3 * left + 2 * right

## part 1
summed = add_all(data.splitlines())
mag = magnitude(eval(summed))
print(mag)

## part 2
from itertools import combinations
mags = []
for a,b in combinations(data.splitlines(),2):
    mags.append(magnitude(eval(add(a,b))))
    mags.append(magnitude(eval(add(b,a))))
print(max(mags))


##### tests ######

## test neighbors
assert left_neighbor('[1,[3,4]]',3) == (1,2)
assert right_neighbor('[1,[3,4],8]',7) == (9,10)
assert left_neighbor('[14,[3,4]]',3) == (1,3)
assert right_neighbor('[1,[3,4],14]',7) == (9,11)
assert right_neighbor('[1,[3,4]]]',7) == (None,None)
## test explode
assert explode('[[[[[9,8],1],2],3],4]') == '[[[[0,9],2],3],4]'
assert explode('[[[[[9,14],1],2],3],4]') == '[[[[0,15],2],3],4]'
assert explode('[7,[6,[5,[4,[3,2]]]]]') == '[7,[6,[5,[7,0]]]]'
assert explode('[7,[6,[5,[14,[3,2]]]]]') == '[7,[6,[5,[17,0]]]]'
assert explode('[[6,[5,[15,[3,2]]]],11]') == '[[6,[5,[18,0]]],13]'
assert explode('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]')\
                == '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'
assert explode('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]')\
                == '[[3,[2,[8,0]]],[9,[5,[7,0]]]]'

assert explode('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]')\
                == '[[[[0,7],4],[7,[[8,4],9]]],[1,1]]'

assert explode('[[[[0,7],4],[7,[[8,4],9]]],[1,1]]') == '[[[[0,7],4],[15,[0,13]]],[1,1]]'

## test split
assert split('[[[[0,7],4],[15,[0,13]]],[1,1]]')\
               ==  '[[[[0,7],4],[[7,8],[0,13]]],[1,1]]'
assert split('[[[[0,7],4],[[7,8],[0,13]]],[1,1]]')\
             == '[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]'

assert add('[[[[4,3],4],4],[7,[[8,4],9]]]','[1,1]') == '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]'

assert(add('[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]',
           '[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]') == \
           '[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]')

ex = """[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]"""

assert add_all(ex.splitlines()) == '[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]'
print('tests pass')