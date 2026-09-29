def linear_search(data, target):
    for index, value in enumerate(data):
        if value == target:
            return index
    return -1

data = [12, 35, 21, 48, 57, 63]
hasil1 = linear_search(data, 48)
hasil2 = linear_search(data, 99)
print('48 berada pada indeks:', hasil1)
print('99 berada pada indeks:', hasil2)