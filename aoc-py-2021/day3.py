from collections import Counter
data = open('day3.txt').read().splitlines()

def common_bits(bits,most=True):
    data = list(zip(*bits))
    mc = [Counter(d).most_common() for d in data]
    mc = [d[0] if most else d[-1] for d in mc]
    mc = [d[0] for d in mc]
    return int("".join(mc),2)


most_common =  common_bits(data,most=True)
least_common = common_bits(data,most=False)

print(most_common * least_common)

## part 2

def get_common(data,most=True):
    c = Counter(data)
    zero,one = c['0'],c['1']
    if most:
        return '1' if one >= zero else '0'
    return '0' if zero <= one else '1'

def rating(data,most=True):
    i = 0
    while len(data) > 1:
        most_common = get_common([d[i] for d in data],most)
        data = [d for d in data if d[i] == most_common]
        i += 1
    return int("".join(data),2)

oxygen = rating(data,most=True)
co2 = rating(data,most=False)
print(oxygen * co2)