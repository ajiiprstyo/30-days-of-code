def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y == 0:
        return "Kesalahan! Pembagian dengan nol."
    return x / y

def kalkulator():
    print("Pilih operasi:")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")

    while True:
        pilihan = input("Masukkan pilihan (1/2/3/4): ")

        if pilihan in ('1', '2', '3', '4'):
            try:
                angka1 = float(input("Masukkan angka pertama: "))
                angka2 = float(input("Masukkan angka kedua: "))
            except ValueError:
                print("Input tidak valid. Silakan masukkan nilai numerik.")
                continue

            if pilihan == '1':
                print(f'{angka1} + {angka2} = {tambah(angka1, angka2)}')
            elif pilihan == '2':
                print(f'{angka1} - {angka2} = {kurang(angka1, angka2)}')
            elif pilihan == '3':
                print(f'{angka1} * {angka2} = {kali(angka1, angka2)}')
            elif pilihan == '4':
                print(f'{angka1} / {angka2} = {bagi(angka1, angka2)}')

            kalkulasi_selanjutnya = input("Apakah Anda ingin melakukan perhitungan lagi? (ya/tidak): ")
            if kalkulasi_selanjutnya.lower() != 'ya':
                break
        else:
            print("Input tidak valid. Silakan pilih operasi yang benar.")

if __name__ == "__main__":
    kalkulator()
  
