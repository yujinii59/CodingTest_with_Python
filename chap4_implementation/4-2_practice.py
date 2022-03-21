h = int(input('측정하고 싶은 마지막 시간을 입력하세요 : '))

cnt = 0
for hour in range(h + 1):
    for minute in range(60):
        for second in range(60):
            if '3' in str(second) + str(minute) + str(hour):
                cnt += 1
                continue
print(cnt)