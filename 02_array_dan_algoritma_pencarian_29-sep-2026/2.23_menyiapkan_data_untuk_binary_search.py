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

nim = ['41250017', '41250003', '41250029', '41250011', '41250008']
target = '41250011'

nim_urut = sorted(nim)
print(nim_urut)

posisi = binary_search(nim_urut, target)
print('Posisi pada data terurut:', posisi)