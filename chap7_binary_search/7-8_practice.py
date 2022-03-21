n, m = map(int, input().split())
lengths = list(map(int, input().split()))

end = max(lengths)
cut_length = sum(lengths)


def binary_search(lengths, target, start, end):
    while True:
        if start >= end:
            return end
        mid = (start + end) // 2
        cut_length = sum((length - mid) for length in lengths if (length - mid) >= 0)

        if cut_length == target:
            return mid
        elif cut_length > target:
            start = mid + 1
        else:
            end = mid - 1
    return None


result = binary_search(lengths, m, 0, end)
print(result)
