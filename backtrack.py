import sys
import time

def find_next_empty(puzzle):
    # mencari baris dan kolom yang belum terisi (direpresentasikan dengan 0)
    # mengembalikan baris, kolom berbentuk tuple atau (None, None) jika tidak ada)

    # melakukan looping pada baris
    for r in range(9):
        # melakukan looping pada kolom
        for c in range(9):
            #mengecek apakah koordinat baris dan kolom tersebut bernilai 0
            #jika iya maka akan mengembalikan nilai baris dan kolom
            if puzzle[r][c] == 0:
                return r, c

    return None, None  # jika tidak ada yang 0, makan akan mengembalikan None, None

def is_valid(puzzle, guess, row, col):
    # mengecek nilai apakah valid atau tidak sesuai aturan pada game sudoku

    # membuat variabel baru untuk menampung nilai baris
    row_vals = puzzle[row]
    if guess in row_vals:
        return False # jika ada dalam satu baris yang nilainya sama, maka akan mengembalikan false

    # membuat variabel baru untuk menampung nilai kolom
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False #jika ada dalam satu kolom yang nilainya sama, maka akan mengembalikan false

    # mengecek setiap kotak 3x3
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    #looping baris pertama sampai ketiga
    for r in range(row_start, row_start + 3):
        #looping kolom pertama sampai ketiga
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False #jika ada nilai yang sama maka mengembalikan false

    return True #jika ada nilai yang sama maka mengembalikan true

def solve_sudoku(puzzle):
    global attempts
    # menyelesaikan sudoku dengan metode backtracking!

    # step 1: mencari titik yang masih kosong
    row, col = find_next_empty(puzzle)

    # step 1.1: jika tidak ada yang kosong, maka artinya sudoku sudah selesai
    if row is None:  # jika tidak ada yang kosong
        return True #akan mereturn true
    
    # step 2: jika masih ada yang kosong, maka masukan tebakan antara 1-9
    for guess in range(1, 10): # range(1, 10) adalah 1, 2, 3, ... 9
        # step 3: mengecek apakah tebakanya benar dan sesuai rules
        if is_valid(puzzle, guess, row, col):
            # step 3.1: jika tebakan benar maka, letakan nilai pada pada koordinat baris dan kolom
            puzzle[row][col] = guess
            attempts += 1  # Tambahkan 1 ke jumlah percobaan bruteforce
            # step 4: mengulang langkah yang sama secara rekursif sampai tidak ada titik yang kosong
            if solve_sudoku(puzzle):
                return True
        
        # step 5: jika tidak ada yang valid atau tidak ditemukan jawaban, maka titik akan diberi nilai 0
        puzzle[row][col] = 0

    # step 6: jika sama sekali tidak ada nilai yang sesuai, makan dapat dinyatakan sudoku tidak dapat dipecahkan
    return False


def open_sudoku_board(filename):

    # membuka file dengan with open nama file
    with open(filename, "r") as file:
        # membaca semua baris dari file
        lines = file.readlines()

        # membuat array baru untuk menampung tiap baris
        array_result = []

        # membaca setiap baris dari file
        for line in lines:
            # menghapus whitespace
            line = line.strip()

            # memisahkan digit menjadi array
            digits = [int(digit) for digit in line]

            # menambahkan digit ke array
            array_result.append(digits)
    
    return array_result

def format_sudoku_array(array):
    # ubah array ke string format tampilan board
    string_format = ""
    for i, row in enumerate(array):
        if i % 3 == 0 and i != 0:
            string_format += "---------------------\n"
        string_format += " ".join(str(num) for num in row[:3]) + " | "
        string_format += " ".join(str(num) for num in row[3:6]) + " | "
        string_format += " ".join(str(num) for num in row[6:9]) + "\n"

    return string_format

if __name__ == '__main__':
        
    attempts = 0
    if len(sys.argv) > 1:
        # membuka file case sudoku sesuai yang diinputkan
        sudoku_board = open_sudoku_board(sys.argv[1])

        #inisialisasi waktu mulai
        start_time = time.time()

        # memecahkan case dengan metode backtracking
        solve_sudoku(sudoku_board)

        #medapatkan waktu selesai
        finish_time = time.time() - start_time
        
        #memformat tampilan board sudoku
        print(format_sudoku_array(sudoku_board))

        # menampilkan waktu yang digunakan untuk menyelesaikan sudoku
        # print(f"Waktu dieksekusi : {finish_time} detik")
        print(f"Waktu dieksekusi {finish_time:.21f} seconds")

        print(f"Percobaan Backtrack: {attempts}")
    else:
        # Cetak pesan penggunaan jika tidak ada argumen yang diberikan
        print('Usage: python sudoku.py puzzle.txt')
