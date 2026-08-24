diagonals = [1]
l = 1
n = 1001

i = 1

while i < n**2:
    if i == (l+2)**2:
        l += 2
    d = i + l + 1
    diagonals.append(d)
    i=d

print(diagonals, sum(diagonals))
