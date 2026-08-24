n = 5
limit = 6*(9**n)
nums = []

for i in range(2, limit + 1):
    total = 0
    for c in str(i):
        dig = int(c)
        total += dig**n
    if total == i:
        nums.append(i)

print(nums, sum(nums))
