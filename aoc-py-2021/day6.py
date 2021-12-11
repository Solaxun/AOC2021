data = open('day6.txt').read().split(',')
nums = [int(x) for x in data]

for i in range(80):
    new_nums = []
    for n in nums:
        if n == 0:
            new_nums.append(6)
            new_nums.append(8)
        else:
            new_nums.append(n-1)
    nums = new_nums

print(len(nums))

## part 2
nums = [int(x) for x in data]
ages = dict(zip(range(9),[0]*9))
for n in nums:
    ages[n] += 1

for i in range(256):
    newfish = ages[0]
    for age in range(1,9):
        ages[age-1] = ages[age]
    ages[6] += newfish
    ages[8] = newfish

print(sum(ages.values()))