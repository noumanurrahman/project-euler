from library.strings import is_palindrome

largest = 0

for i in range(999, 99, -1):
    for j in range(990, 99, -11):
        product = i * j
        if is_palindrome(str(product)):
            if largest < product:
                largest = product

print(largest)