from math import factorial

total = 0

for i in range(145, factorial(9)*9):
    digits = [int(j) for j in str(i)]
    s = 0
    for d in digits:
        s += factorial(d)
    if s == i:
        total += i

print(total)
