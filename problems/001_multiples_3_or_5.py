def multiple_3_or_5(x: int) -> bool:
    if x % 3 == 0 or x % 5 == 0:
        return True
    return False


result = 0

for i in range(1, 1000):
    if multiple_3_or_5(i):
        result += i

print(result)