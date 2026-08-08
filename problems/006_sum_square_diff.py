target = 100
sq_sum = 0
total = 0
for i in range(1, target + 1):
    sq_sum += i*i
    total += i

total_sq = total * total
print(total_sq - sq_sum)