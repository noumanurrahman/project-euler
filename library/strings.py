def is_palindrome(s: str) -> bool:
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

def numbers_to_letters(n: int) -> str:
    if n == 0:
        return "zero"
    if n < 0:
        return "negative " + numbers_to_letters(-n)
    if n == 1000:
        return "one thousand"

    ones = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
    }
    teens = {
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
    }
    tens = {
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
    }

    words = []

    if n >= 100:
        words.append(ones[n // 100])
        words.append("hundred")
        n %= 100

        if n:
            words.append("and")

    if 10 <= n <= 19:
        words.append(teens[n])
    elif n >= 20:
        words.append(tens[n // 10 * 10])
        n %= 10

        if n:
            words.append(ones[n])
    elif n > 0:
        words.append(ones[n])

    return " ".join(words)