s = input('여러개의 숫자로 구성된 문자열 입력: ')
result = 0
for num in s:
    num = int(num)
    if result + num > result * num:
        result += num
    else:
        result *= num

print(result)