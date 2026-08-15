from math import factorial

n, r = 40, 20
c = factorial(n) // (factorial(r) * factorial(n - r))
print(c)