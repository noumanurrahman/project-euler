def get_cycle_length(d):
    seen_remainders = {}
    remainder = 1
    position = 0
    
    while remainder != 0 and remainder not in seen_remainders:
        seen_remainders[remainder] = position
        remainder = (remainder * 10) % d
        position += 1
        
    if remainder == 0:
        return 0
    return position - seen_remainders[remainder]

max_length = 0
answer = 0
for d in range(999, 1, -1):
    if max_length >= d:
        break
        
    length = get_cycle_length(d)
    if length > max_length:
        max_length = length
        answer = d

print(answer)
