x = int(input())

cntls = [0] * (x + 1)
cntls[1] = 0

for i in range(2, x + 1):
    cnt_d5 = cnt_d3 = cnt_d2 = cnt_m1 = x + 1
    if i % 5 == 0:
        cnt_d5 = cntls[i // 5] + 1
    if i % 3 == 0:
        cnt_d3 = cntls[i // 3] + 1
    if i % 2 == 0:
        cnt_d2 = cntls[i // 2] + 1
    cnt_m1 = cntls[i - 1] + 1
    cnt = min(cnt_d5, cnt_d3, cnt_d2, cnt_m1)

    if cntls[i] != 0:
        cntls[i] = min(cntls[i], cnt)
    else:
        cntls[i] = cnt

print(cntls[x])
