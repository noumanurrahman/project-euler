from library.numbers import find_primes


def highest_power(p: int) -> int:
    power = 1
    while p ** power <= limit:
        power += 1
    return power - 1

def is_evenly_divisible(n: int, k: int) -> bool:
    for i in range(1, k + 1):
        if n % i != 0:
            return False
    return True

limit = 20
primes = find_primes(limit)

result = 1
for prime in primes:
    result *= pow(prime, highest_power(prime))

print(result)