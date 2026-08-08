def even_fibonacci(n: int) -> list[int]:
    seq = [2]
    prev = 1
    curr = seq[0]
    while True:
        prev, curr = curr, prev + curr
        if curr >= n:
            break
        if curr % 2 == 0:
            seq.append(curr)
    return seq

print(sum(even_fibonacci(4000000)))