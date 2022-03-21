n = int(input())
stored_fodds = list(map(int, input().split()))

d = [0] * n
d[0] = stored_fodds[0]
d[1] = max(stored_fodds[0], stored_fodds[1])

for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + stored_fodds[i])

print(d[n - 1])