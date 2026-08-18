from library.numbers import find_factors

pairs = []
nums = []
limit = 10000

for i in range(1, limit):
    factors = find_factors(i)
    total = sum(factors) - i
    nums.append(total)

for a in range(1, limit):
    for b in range(1, limit):
        if a != b and nums[a - 1] == b and nums[b - 1] == a:
            pairs.append(a)
            pairs.append(b)

print(sum(set(pairs)))