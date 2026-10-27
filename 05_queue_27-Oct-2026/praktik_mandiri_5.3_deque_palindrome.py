from collections import deque

def is_palindrome(text):
    chars = deque(c.lower() for c in text if c.isalnum())

    while len(chars) > 1:
        if chars.popleft() != chars.pop():
            return False
    return True


def is_palindrome_trace(text):
    """Versi yang menampilkan pasangan kiri-kanan pada setiap iterasi."""
    chars = deque(c.lower() for c in text if c.isalnum())
    langkah = 1

    while len(chars) > 1:
        kiri = chars.popleft()
        kanan = chars.pop()
        status = 'sama' if kiri == kanan else 'BEDA'
        print(f'  Iterasi {langkah}: kiri={kiri!r}, kanan={kanan!r} '
              f'-> {status}, sisa={list(chars)}')
        if kiri != kanan:
            return False
        langkah += 1

    return True


# 1. Fungsi is_palindrome() mengikuti contoh modul bagian 5.20.

# 2. Uji kata: level, katak, radar, python, algoritma.
print('== Uji kata ==')
for kata in ['level', 'katak', 'radar', 'python', 'algoritma']:
    print(f'{kata:<10} :', is_palindrome(kata))

# 3. Uji kalimat yang mengandung spasi atau tanda baca.
print('\n== Uji kalimat (setelah normalisasi) ==')
kalimat = [
    'Kasur ini rusak!',
    'A man, a plan, a canal: Panama',
    'No lemon, no melon',
    'Struktur Data',
]
for teks in kalimat:
    print(f'{teks!r:<38} :', is_palindrome(teks))

# 4 dan 5. Dry run pasangan karakter dengan fungsi yang menampilkan setiap iterasi.
print('\n== Trace pasangan karakter ==')
for teks in ['katak', 'level']:
    print(f'{teks!r}:')
    print('  Hasil :', is_palindrome_trace(teks))

# 6. Deque lebih natural daripada Queue satu arah karena palindrome perlu
#    membandingkan dua ujung sekaligus. Queue hanya bisa mengakses front,
#    sedangkan deque menyediakan popleft() dan pop() yang keduanya O(1).

# 7. Kompleksitas waktu O(n) karena setiap karakter masuk sekali dan keluar
#    paling banyak sekali. Kompleksitas ruang O(n) untuk menyimpan karakter.
