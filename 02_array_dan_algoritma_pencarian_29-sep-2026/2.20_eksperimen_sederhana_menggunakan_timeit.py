import timeit

def linear_search(data, target):
    for index, value in enumerate(data):
        if value == target:
            return index
    return -1

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

data = list(range(100_000))
target = -1

waktu_linear = timeit.timeit(
    lambda: linear_search(data, target),
    number=100
)

waktu_binary = timeit.timeit(
    lambda: binary_search(data, target),
    number=100
)

print('Linear Search:', waktu_linear)
print('Binary Search:', waktu_binary)