n, m = map(int, input().split())

coins = list()
for _ in range(n):
    coins.append(int(input()))

d = [0] * (m + 1)
for i in range(1, m + 1):
    for coin in coins:
        if i >= coin:
            if d[i] != -1:
                d[i] = min(d[i], d[i - coin] + 1)
            else:
                d[i] = d[i - coin] + 1
if d[m] == 0:
    print(-1)
else:
    print(d[m])