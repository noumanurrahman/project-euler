def collatz_sequence(n):
    terms = [n]
    current = n

    while current != 1:
        if current % 2 == 0:
            current = current // 2
        else:
            current = (3 * current) + 1
        terms.append(current)

    return terms

longest = 0
answer = 0

for i in range(1000000, 1, -1):
    sequence = collatz_sequence(i)
    if len(sequence) > longest:
        longest = len(sequence)
        answer = i

print(answer, longest)