tri_nums = []

for i in range(1, 30):
    t = (i/2) * (i + 1)
    tri_nums.append(t)

with open("../extra/words.txt", "r") as f:
    words = f.read().replace('"', '').replace('\n', '').split(',')

answer = 0

for word in words:
    value = 0
    for char in word:
        pos = ord(char.lower()) - ord('a') + 1
        value += pos
    if value in tri_nums:
        answer += 1

print(answer)
