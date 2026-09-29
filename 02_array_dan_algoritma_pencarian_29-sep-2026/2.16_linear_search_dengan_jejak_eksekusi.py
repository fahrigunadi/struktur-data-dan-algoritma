def linear_search_trace(data, target):
    for index, value in enumerate(data):
        print('Periksa indeks', index, 'nilai', value)
        if value == target:
            print('Target ditemukan')
            return index
    print('Target tidak ditemukan')
    return -1

linear_search_trace([7, 11, 15, 18, 25, 30], 25)