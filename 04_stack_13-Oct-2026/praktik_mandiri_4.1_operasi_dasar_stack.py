# 1. Buat class Stack menggunakan Python list.
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)


# 2. Tambahkan data 10, 20, 30, 40 menggunakan push.
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
print('Isi stack :', stack.items)

# 3. Tampilkan top dan size.
print('Top  :', stack.peek())
print('Size :', stack.size())

# 4. Lakukan pop dua kali dan catat urutan nilai yang keluar.
print('Pop ke-1 :', stack.pop())
print('Pop ke-2 :', stack.pop())
print('Sisa     :', stack.items)

# 5. Tambahkan data 50 dan 60.
stack.push(50)
stack.push(60)
print('Isi stack :', stack.items)

# 6. Loop yang mengeluarkan semua elemen sampai Stack kosong.
print('Mengeluarkan semua elemen:')
while not stack.is_empty():
    print('  Pop :', stack.pop())
print('Stack kosong :', stack.is_empty())

# 7. Uji pop ketika Stack kosong dan jelaskan perilakunya.
hasil = stack.pop()
print('Pop saat kosong :', hasil)
# Penjelasan: pop() dipanggil ketika Stack kosong TIDAK error karena method
# memeriksa is_empty() lebih dulu, lalu mengembalikan None. Nilai size tetap 0.
print('Size setelah pop kosong :', stack.size())
