from math import log
from library.numbers import find_primes

n = 10001
limit = int(n * (log(n) + log(log(n))))
primes = find_primes(limit)
print(primes[n-1])