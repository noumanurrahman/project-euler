def find_primes(n:int) -> list[int]:
    odd_nums = range(2, (n + 1)//2)
    is_prime = [True for _ in range(n + 1)]

    for i in odd_nums:
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return [i for i in range(2, n + 1) if is_prime[i]]

def find_prime_factors(n: int) -> list[int]:
    factors = []
    divisor = 3

    if n % 2 == 0:
        factors.append(2)
        while n % 2 == 0:
            n //= 2

    while divisor * divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            while n % divisor == 0:
                n //= divisor
        divisor += 2

    if n > 1:
        factors.append(n)

    return factors

def find_factors(n: int) -> list[int]:
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    return sorted(factors)