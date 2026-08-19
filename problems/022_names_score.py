with open("../extra/names.txt", "r") as f:
    names = f.read().replace('"', '').split(',')
    names.sort()

total_score = 0

for i, name in enumerate(names):
    value = sum(ord(letter.lower()) - 96 for letter in name)
    score = value * (i + 1)
    total_score += score

print(total_score)