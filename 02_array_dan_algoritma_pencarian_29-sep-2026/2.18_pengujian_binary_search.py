def binary_search(data, target):
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

data = [12, 18, 25, 31, 44, 57, 63, 70, 82]

print(binary_search(data, 57))
print(binary_search(data, 13))