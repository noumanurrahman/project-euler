from math import factorial

n = 100
digits = [int(d) for d in str(factorial(n))]
print(sum(digits))