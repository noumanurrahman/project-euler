pints = [1, 2, 5, 10, 20, 50]
pounds = []
target = 2
t = target * 100

p = 1
while p <= target:
    pound = p * 100
    pounds.append(pound)
    p += 1

coins = pints + pounds

ways = [0] * (t+1)
ways[0] = 1

for coin in coins:
    for amount in range(coin, t + 1):
        ways[amount] += ways[amount - coin]

print(ways[200])