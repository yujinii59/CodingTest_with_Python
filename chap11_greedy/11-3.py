str = input()

lnum = str[0]
lb = -1
result = 0
for i, num in enumerate(str):
    if lnum != num:
        if lb == -1:
            lb = i
            result += 1
        else:
            lb = -1
    lnum = num

print(result)