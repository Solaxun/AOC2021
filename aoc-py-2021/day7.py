data = open('day7.txt').read().split(',')
nums = [int(x) for x in data]

i, all_costs = 0, []
while i < len(nums):
    cost = 0
    for n in nums:
        cost += abs(nums[i] - n)
    all_costs.append([i,cost])
    i += 1

ans = min(all_costs,key=lambda x: x[1])
print(ans)

# part 2
i, all_costs = 0, []
while i < len(nums):
    cost = 0
    for n in nums:
        a,b = sorted([nums[i],n])
        cost += sum(range(b-a+1))
    all_costs.append([i,cost])
    i += 1
ans = min(all_costs,key=lambda x: x[1])
print(ans)