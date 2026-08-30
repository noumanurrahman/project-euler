string = ""

i = 1
while True:
    string += str(i)
    if len(string) >= 10**6:
        break
    i += 1

answer = int(string[0]) * int(string[9]) * int(string[99]) * int(string[999]) * int(string[9999]) * int(string[99999]) * int(string[999999])
print(answer)
