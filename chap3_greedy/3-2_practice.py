n, m, k = map(int, input().split())
array = list(map(int, input().split()))

array.sort()
first = array[-1]
second = array[-2]

sum = first * (m // (k + 1) * k + m % (k + 1))
sum += second * (m // (k + 1))

print(sum)