n, m = map(int, input().split())
weights = list(map(int, input().split()))

weights.sort()

count = 0
for i in range(len(weights)):
    for j in range(i + 1, len(weights)):
        if weights[i] != weights[j]:
            count += 1

print(count)