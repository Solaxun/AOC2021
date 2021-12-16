from collections import defaultdict
data = open('day14.txt').read().splitlines()
poly, _, *reactions = data
reactions = dict(r.split(' -> ') for r in reactions)

def step(pcounts):
  pcounts_new = defaultdict(int)
  for p,cnt in pcounts.items():
    r = reactions[p]
    pcounts_new[p[0] + r] += cnt
    pcounts_new[r + p[1]] += cnt
  return pcounts_new

start = defaultdict(int)
for i in range(len(poly) - 1):
    p = poly[i:i+2]
    start[p] += 1

polycnt = start
for i in range(40): # change to 10 for part 1
  polycnt = step(polycnt)

letters = set(l for pair in reactions.keys() for l in pair)
totals = dict(zip(letters,[0]*len(letters)))

for pair,cnt in polycnt.items():
  a,b = pair
  totals[a] += cnt
totals[b] += 1
print(totals[max(totals,key=totals.get)] - 
      totals[min(totals,key=totals.get)])

## looked at forum to figure it out

## was stuck here... if dict keeping track then orderings won't
## be same, e.g. {NN,CB} yields diff poly than {CB,NN}:

# NNCB -> NN CB -> NN NC CB -> NCN NBC CHB -> NCNBCHB
# doees diff order produce same poly? 
# CBNN -> CB NN -> CB BN NN -> CHB BBN NCN -> CHBBNCN
# on next iter, "BB" is in the below chain but not above chain
# which will yield a diff production

## solution:  
# NN NC CB -> split into unique pairs it forms
# NN: [NC CN], NC: [NB BC], CB: [CH, HB]
# then just increment counts.. if we have 3 NC then it will 
# create [NB BC] 3 times