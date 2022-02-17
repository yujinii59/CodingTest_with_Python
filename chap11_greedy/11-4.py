n = int(input())
numbers = list(map(int, input().split()))

numbers.sort(reverse=True)

i = 1
summary = sum(numbers)
while i < summary:
    sum = 0
    num = i
    for number in numbers:
        if number <= num:
            num -= number

    if num != 0:
        break
    i += 1
print(i)