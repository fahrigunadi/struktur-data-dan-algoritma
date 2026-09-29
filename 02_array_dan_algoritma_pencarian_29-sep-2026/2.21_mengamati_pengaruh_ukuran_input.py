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

for n in [1_000, 10_000, 100_000]:
    data = list(range(n))
    target = -1

    t_linear = timeit.timeit(
        lambda: linear_search(data, target),
        number=100
    )

    t_binary = timeit.timeit(
        lambda: binary_search(data, target),
        number=100
    )

    print('n =', n)
    print(' linear:', t_linear)
    print(' binary:', t_binary)