data = open('day1.txt').read().splitlines()
data = [int(a) for a in data]

cnt = 0
for a,b in zip(data,data[1:]):
    if b > a:
        cnt += 1

print(cnt)

cnt, prevsum = 0,0
for i in range(len(data)-3):
    total = sum(data[i:i+3])
    if total > prevsum:
        cnt +=1
    prevsum = total

print(cnt)