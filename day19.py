def apakah_bilangan_prima(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def tampilkan_bilangan_prima(awal, akhir):
    print(f"Bilangan prima antara {awal} dan {akhir}:")
    for num in range(awal, akhir + 1):
        if apakah_bilangan_prima(num):
            print(num, end=' ')
    print()

def main():
    while True:
        print("\n--- PROGRAM BILANGAN PRIMA ---")
        print("1. Cek Bilangan Prima")
        print("2. Tampilkan Bilangan Prima dalam Rentang")
        print("3. Keluar")
        pilihan = input("Pilih opsi (1/2/3): ")

        if pilihan == '1':
            try:
                angka = int(input("Masukkan angka untuk diperiksa: "))
                if apakah_bilangan_prima(angka):
                    print(f"{angka} adalah bilangan prima.")
                else:
                    print(f"{angka} bukan bilangan prima.")
            except ValueError:
                print("Input tidak valid. Silakan masukkan angka yang benar.")

        elif pilihan == '2':
            try:
                awal = int(input("Masukkan awal rentang: "))
                akhir = int(input("Masukkan akhir rentang: "))
                if awal > akhir:
                    print("Rentang tidak valid. Pastikan awal kurang dari atau sama dengan akhir.")
                else:
                    tampilkan_bilangan_prima(awal, akhir)
            except ValueError:
                print("Input tidak valid. Silakan masukkan angka yang benar.")

        elif pilihan == '3':
            print("Terima kasih telah menggunakan program ini!")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih opsi yang tersedia.")

if __name__ == "__main__":
    main()
  
