n, m = map(int, input().split())

num = 0
cards = list()
for i in range(n):
    cardls = list(map(int, input(f'{m}개의 정수 입력: ').split()))
    cards.append(cardls)
    cardls.sort()
    min_num = cardls[0]
    num = max(num, min_num)

print(num)

