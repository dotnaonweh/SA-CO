import sys
import time


def sameRow(i, j):
    # Cek apakah dua posisi berada di baris yang sama
    return (i // 9 == j // 9)


def sameCol(i, j):
    # Cek apakah dua posisi berada di kolom yang sama
    return ((i - j) % 9 == 0)


def sameBlock(i, j):
    # Cek apakah dua posisi berada di blok yang sama
    return (i // 27 == j // 27 and i % 9 // 3 == j % 9 // 3)


def solver(check):
    global attempts  # Mendeklarasikan variabel attempts sebagai variabel global
    i = check.find('0')  # Cari posisi angka 0 (tempat yang harus diisi)
    if i == -1:
        printBoard(check)  # Jika tidak ada angka 0 lagi, cetak papan sudoku

    exclude = set()
    # Cek semua posisi dalam papan sudoku
    for j in range(81):
        if sameRow(i, j) or sameCol(i, j) or sameBlock(i, j):
            # Tambahkan angka-angka yang tidak bisa digunakan ke dalam set exclude
            exclude.add(check[j])

    for m in '123456789':
        if m not in exclude:
            attempts += 1  # Tambahkan 1 ke jumlah percobaan bruteforce
            # Rekursif panggil solver() dengan mengisi angka yang valid ke posisi i
            solver((check[:i] + m + check[i + 1:]))


def printBoard(check):
    for i in range(9):
        for j in range(9):
            # Cetak angka di setiap posisi dalam papan sudoku
            print(check[i * 9 + j], end=' ')
            if j % 3 == 2 and j != 8:
                # Cetak '|' setelah setiap 3 kolom, kecuali kolom terakhir
                print('|', end=' ')
        print()  # Cetak newline setelah setiap baris
        if i % 3 == 2 and i != 8:
            # Cetak '-------' setelah setiap 3 baris, kecuali baris terakhir
            print('-' * 21)


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as file:
        # Baca puzzle dari file dan hapus karakter newline
        puzzle = file.read().replace('\n', '')
        # Inisialisasi jumlah percobaan bruteforce
        attempts = 0
        # Waktu mulai eksekusi
        startTime = time.time()
        solver(puzzle)
        # Waktu selesai eksekusi
        endTime = time.time()
        execTime = endTime - startTime
        # Menampilkan berapa waktu yang dibutuhkan dan berapa jumlah percobaan bruteforce
        print(f"Waktu dieksekusi : {execTime} detik")
        print(f"Percobaan BruteForce: {attempts}")

else:
    # Cetak pesan penggunaan jika tidak ada argumen yang diberikan
    print('Usage: python sudoku.py puzzle.txt')
