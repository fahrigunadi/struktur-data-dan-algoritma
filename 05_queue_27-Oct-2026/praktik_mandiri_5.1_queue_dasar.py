from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.popleft()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]

    def size(self):
        return len(self.items)


# 1. Class Queue berbasis collections.deque sudah dibuat di atas,

# 2. Masukkan data 10, 20, 30, 40, 50.
q = Queue()
for x in [10, 20, 30, 40, 50]:
    q.enqueue(x)
print('Isi queue :', q.items)

# 3. Tampilkan front dan size.
print('Front :', q.peek())
print('Size  :', q.size())

# 4. Lakukan dequeue dua kali dan catat nilai yang keluar.
keluar_1 = q.dequeue()
keluar_2 = q.dequeue()
print('Dequeue ke-1 :', keluar_1)
print('Dequeue ke-2 :', keluar_2)
print('Isi queue    :', q.items)

# 5. Tambahkan 60 dan 70.
q.enqueue(60)
q.enqueue(70)
print('Isi queue :', q.items)

# 6. Keluarkan seluruh elemen dengan loop sampai Queue kosong.
print('Mengeluarkan seluruh elemen:')
while not q.is_empty():
    print('  Dequeue :', q.dequeue())
print('Queue kosong :', q.is_empty())

# 7. Uji dequeue dan peek ketika Queue kosong.
print('Dequeue saat kosong :', q.dequeue())
print('Peek saat kosong    :', q.peek())
print('Size saat kosong    :', q.size())
