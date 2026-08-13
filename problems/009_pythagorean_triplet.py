a, b, c = 0, 0, 0

for i in range(1, 997+1):
    for j in range(1, 997+1):
        if i == j:
            continue
        # see notes/problems/009.md
        if i*j - 1000 * (i+j) + 500000 == 0:
            a, b, c = i, j, 1000 - i - j
            break

print(a, b, c)
print(a * b * c)