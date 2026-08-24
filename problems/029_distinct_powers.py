n = 100
nums = []

for a in range(2, n + 1):
    for b in range(2, n + 1):
        nums.append(a**b)

nums = list(set(nums))
print(len(nums))
