n = int(input())

d = [0] * (n + 1)
d[1] = 1
d[2] = 3

for i in range(3, n + 1):
    cnt = d[i - 1] * d[1]
    cnt += d[i - 2] * (d[2] - 1)
    d[i] = cnt % 796796

print(d[n])
