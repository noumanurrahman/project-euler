from itertools import compress

abundant_nums = []

for i in range(1, 28124):
    factors = []
    for j in range(1, i):
        if i % j == 0:
            factors.append(j)
    if sum(factors) > i:
        abundant_nums.append(i)

sums = [True]*28123
k = 0
for i in abundant_nums:
    for j in abundant_nums[k:]:
        if i+j>28123: break
        sums[i+j-1] = False
    k+=1

answer = sum(compress(range(1,28124), sums))

print(answer)
