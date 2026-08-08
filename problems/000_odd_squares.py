def find_odd_square(x: int) -> int | None:
    sq = x * x
    if sq % 2 != 0:
        return sq
    return None


result = 0
n = 570000

for i in range(1, n+1):
    square = find_odd_square(i)
    if square is not None:
        result += square

print(result)