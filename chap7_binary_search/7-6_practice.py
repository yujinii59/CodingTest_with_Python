n = int(input())
store_items = list(map(int, input().split()))

m = int(input())
check_items = list(map(int, input().split()))

k = max(max(check_items), max(store_items))

sort_array = [0] * k

for item in store_items:
    sort_array[item] += 1

for item in check_items:
    if sort_array[item] == 0:
        print('no', end=' ')
    else:
        print('yes', end=' ')