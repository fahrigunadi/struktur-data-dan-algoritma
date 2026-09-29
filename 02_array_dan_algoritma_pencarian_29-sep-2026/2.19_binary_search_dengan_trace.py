def binary_search_trace(data, target):
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2
        print('left=', left, 'right=', right, 'mid=', mid, 'nilai=', data[mid])

        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

binary_search_trace([12,18,25,31,44,57,63,70,82], 57)