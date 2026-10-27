class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.rear = 0
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.capacity

    def enqueue(self, data):
        if self.is_full():
            return False
        self.items[self.rear] = data
        self.rear = (self.rear + 1) % self.capacity
        self.count += 1
        return True

    def dequeue(self):
        if self.is_empty():
            return None
        data = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return data

    def peek(self):
        if self.is_empty():
            return None
        return self.items[self.front]

    def size(self):
        return self.count


def tampilkan_state(label, cq):
    """Menampilkan keadaan internal dan urutan logis Queue."""
    urutan_logis = [cq.items[(cq.front + i) % cq.capacity] for i in range(cq.count)]
    print(f'{label:<16} items={cq.items} front={cq.front} rear={cq.rear} '
          f'count={cq.count} logis={urutan_logis}')


# 1. Buat CircularQueue dengan kapasitas 4.
cq = CircularQueue(4)
tampilkan_state('Awal', cq)

# 2. Enqueue A, B, C, D dan cek kondisi penuh.
for data in ['A', 'B', 'C', 'D']:
    cq.enqueue(data)
    tampilkan_state(f'enqueue {data}', cq)
print('is_full :', cq.is_full())

# 3. Coba enqueue E ketika penuh dan catat hasilnya.
hasil = cq.enqueue('E')
print('enqueue E saat penuh :', hasil)
tampilkan_state('setelah coba E', cq)

# 4. Dequeue dua elemen.
print('dequeue ke-1 :', cq.dequeue())
tampilkan_state('dequeue ke-1', cq)
print('dequeue ke-2 :', cq.dequeue())
tampilkan_state('dequeue ke-2', cq)

# 5. Enqueue E dan F sehingga rear melakukan wrap-around.
print('enqueue E :', cq.enqueue('E'))
tampilkan_state('enqueue E', cq)
print('enqueue F :', cq.enqueue('F'))
tampilkan_state('enqueue F', cq)

# 6. Keadaan items, front, rear, dan count sudah ditampilkan setelah setiap operasi.

# 7. Gambaran array fisik dan urutan logis.
print('Array fisik   :', cq.items)
print('Urutan logis  :', [cq.items[(cq.front + i) % cq.capacity] for i in range(cq.count)])

# 8. Operasi modulo membuat indeks rear dan front kembali ke 0 setelah mencapai
#    kapasitas - 1, sehingga slot kosong di awal array dapat dipakai lagi.

# 9. Kompleksitas enqueue dan dequeue adalah O(1) karena hanya mengakses satu
#    indeks dan melakukan operasi aritmetika modulo tanpa menggeser elemen.
