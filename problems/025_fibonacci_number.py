def fibonacci(n: int) -> list[int]:
    seq = [1]
    prev = 0
    curr = 1
    while True:
        prev, curr = curr, prev + curr
        if curr >= n:
            break
        seq.append(curr)
    return seq
n = 1000
sequence = fibonacci(10**n)
print(sequence)
for i, num in enumerate(sequence):
    if len(str(num)) >= n:
        print(len(str(num)))
        print(f"Index: {i+1}, Number: {num}")
        break