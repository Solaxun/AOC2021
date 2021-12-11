data = open('day8.txt').read().splitlines()
data = [line.split(' | ') for line in data]

num_to_len = {1:2,4:4,7:3,8:7}

def unique_digits(numseq):
    return len(numseq) in set(num_to_len.values())

res = [fourd if unique_digits(fourd) else None
              for (sig_pattern, four_digit_outputs) in data 
              for fourd in four_digit_outputs.split(' ')]

res = [r for r in res if r]
print(len(res))

## part 2
import itertools

# arbitrary ordering - start at top center and increase indices clockwise with
# middle section of digit as last index. 
ixs_to_num =  {
  (0,1,2,3,4,5):0,
  (1,2):1,
  (0,1,3,4,6):2,
  (0,1,2,3,6):3,
  (1,2,5,6):4,
  (0,2,3,5,6):5,
  (0,2,3,4,5,6):6,
  (0,1,2):7,
  (0,1,2,3,4,5,6):8,
  (0,1,2,3,5,6):9
}

def valid_number(letter,config):
  ixs = tuple(sorted(config.index(l) for l in letter))
  return ixs_to_num.get(ixs)

def gen_lookup(segments):
  eight = list('abcdefg')
  for config in itertools.permutations(eight):
    res = {'abcdefg':8}
    for s in [s for s in segments if len(s) != 7]:
      v = valid_number(s,config)
      if v is not None:
        # sort so we can look up right side here
        res["".join(sorted(s))]=v
    if len(res) == 10:
      return res

def list_to_num(lst):
    # removes leading zeroes but since we are just summing results it
    # doesn't matter e.g. 0743 == 743 is fine when summing. 
    return int("".join([str(n) for n in lst]))

answers = []
for left,right in data:
    lkp = gen_lookup(left.split())
    right = [lkp.get("".join(sorted(r))) for r in right.split()]
    answers.append(list_to_num(right))
print(sum(answers))