def selection_sort_stats(data):
    comparisons = 0
    swaps = 0
    n = len(data)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            comparisons += 1
            if data[j] < data[min_index]:
                min_index = j

        data[i], data[min_index] = data[min_index], data[i]
        swaps += 1

    return data, comparisons, swaps


uji_urut = [1, 2, 3, 4, 5, 6]
uji_acak = [4, 1, 6, 2, 5, 3]
uji_terbalik = [6, 5, 4, 3, 2, 1]

for nama, data in [('terurut', uji_urut), ('acak', uji_acak), ('terbalik', uji_terbalik)]:
    hasil, comparisons, swaps = selection_sort_stats(data)
    print(f'{nama:<9} : {hasil}')
    print(f'{"":<9}   comparisons={comparisons}, swaps={swaps}')
