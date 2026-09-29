def linear_search(data, target):
    for index, value in enumerate(data):
        if value == target:
            return index
    return -1