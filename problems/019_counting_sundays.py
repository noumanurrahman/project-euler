def days_in_month(m: int, year: int) -> int:
    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif m in [4, 6, 9, 11]:
        return 30
    elif m == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return 29
        else:
            return 28

firsts = []
days= 1

for year in range(1900, 2001):
    for month in range(1, 13):
        if year != 1900:
            firsts.append(days)
        days += days_in_month(month, year)

sundays = list(filter(lambda x: x % 7 == 0, firsts))

print(len(sundays))
