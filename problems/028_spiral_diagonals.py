n = 1001
l = (n - 1)//2
s = 1

for i in range(1, l+1):
    s += 16*(i**2) + 4*i + 4

print(s)
