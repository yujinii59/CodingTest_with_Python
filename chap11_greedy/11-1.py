n = int(input('모험가 수를 입력해주세요.: '))
people = list(map(int, input().split()))

people.sort()
num = 0
pcnt = 0
count = 0
for person in people:
    if person > num:
        num = person
    pcnt += 1

    if pcnt == num:
        pcnt = 0
        count += 1

print(count)
