from library.numbers import find_factors

nums = []
prev = 0
i = 1

answer = 0

while True:
    nums.append(prev + i)
    prev = nums[i-1]
    if len(find_factors(nums[i-1])) > 500:
        answer = nums[i-1]
        break
    i+=1

print(answer)