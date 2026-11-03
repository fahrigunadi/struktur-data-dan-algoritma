def bubble_sort_desc(data):
    n = len(data)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            # Kondisi dibalik: tukar jika elemen kiri lebih kecil.
            if data[j] < data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

        print(f'Pass {i + 1}:', data)

    return data


data = [17, 4, 25, 9, 13, 2]
# Target output: [25, 17, 13, 9, 4, 2]
print('Awal  :', data)
print('Hasil :', bubble_sort_desc(data))
