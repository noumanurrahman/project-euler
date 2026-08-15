from library.strings import numbers_to_letters

total_letters = 0

for i in range(1, 1000 + 1):
    text = numbers_to_letters(i)
    letters = len(text.replace(" ", ""))
    total_letters += letters

print(total_letters)
