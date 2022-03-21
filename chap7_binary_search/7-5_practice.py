# 매장 내 부품의 개수
n = int(input())
store_items = list(map(int, input().split()))

# 손님이 원하는 부품의 개수
m = int(input())
order_items = list(map(int, input().split()))

store_items.sort()


def binary_search(array, target, start, end):
    if start > end:
        return None
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None


for order in order_items:
    result = binary_search(store_items, order, 0, n - 1)

    if result is None:
        print('no', end=' ')
    else:
        print('yes', end=' ')
