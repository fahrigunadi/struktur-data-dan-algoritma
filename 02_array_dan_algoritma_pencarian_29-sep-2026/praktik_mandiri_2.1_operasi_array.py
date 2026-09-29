# 1. Buat list nilai yang berisi minimal 10 nilai integer
nilai = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nilai)

# 2. Tampilkan elemen pertama, elemen ke-5, dan elemen terakhir.
print('pertama: ', nilai[0])
print('kelima: ', nilai[4])
print('terakhir: ', nilai[len(nilai) - 1])

# 3. Ubah nilai pada salah satu indeks lalu tampilkan list setelah perubahan.
nilai[3] = 33
print(nilai)

# 4. Tambahkan dua nilai menggunakan append().
nilai.append(11)
nilai.append(12)
print(nilai)

# 5. Sisipkan satu nilai pada indeks 2 menggunakan insert() dan amati perubahan posisi elemen.
nilai.insert(2, 22)
print('setelah insert')
print(nilai)

# 6. Hapus satu elemen dengan pop() dan satu elemen dengan remove()
dihapus = nilai.pop(2)
print('dihapus: ', dihapus)
print('nilai setelah pop: ', nilai)
nilai.remove(33)
print('nilai setelah remove: ', nilai)

# 7. Lakukan traversal menggunakan enumerate() sehingga setiap baris menampilkan indeks dan nilai.
for i, x in enumerate(nilai):
    print('Indeks', i, 'nilai', x)

# 8. Tulis komentar singkat di notebook mengenai operasi mana yang dapat menyebabkan pergeseran elemen.
# insert, pop dan remove