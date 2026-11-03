def insertion_sort_shifts(data):
    shifts = 0

    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            shifts += 1
            j -= 1

        data[j + 1] = key

    return data, shifts


hampir = [1, 2, 3, 5, 4, 6, 7, 8]
acak = [7, 2, 8, 1, 5, 3, 6, 4]
dua_puluh = [15, 3, 9, 1, 20, 7, 12, 5, 18, 2, 11, 8, 16, 4, 19, 6, 14, 10, 17, 13]

for nama, data in [('hampir', hampir), ('acak', acak), ('20 elemen', dua_puluh)]:
    hasil, shifts = insertion_sort_shifts(data)
    print(f'{nama:<10} : {hasil}')
    print(f'{"":<10}   shifts={shifts}')
