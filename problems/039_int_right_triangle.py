from math import sqrt

max_length = 0
answer = 0
for p in range(1, 1000+1):
    solutions = []
    for a in range(1, p):
        for b in range(a, p):
            c = sqrt(a**2 + b**2)
            if a+b+c != p:
                continue
            solutions.append((a, b, c))
    if len(solutions) > max_length:
        max_length = len(solutions)
        answer = p

print(answer, max_length)
