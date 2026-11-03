def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort_trace(data, depth=0):
    indent = ' ' * depth
    print(indent + 'masuk:', data)

    if len(data) <= 1:
        print(indent + 'return:', data)
        return data

    mid = len(data) // 2
    left = merge_sort_trace(data[:mid], depth + 1)
    right = merge_sort_trace(data[mid:], depth + 1)
    result = merge(left, right)

    print(indent + 'merge :', result)
    return result


data = [21, 4, 16, 8, 15, 2, 10, 7]
merge_sort_trace(data)
