def apakah_prima(n):
    # Bilangan kurang dari 2 bukan bilangan prima
    if n < 2:
        print("Bukan Bilangan Prima")
        return

    # Memeriksa apakah ada pembagi selain 1 dan n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print("Bukan Bilangan Prima")
            return
    
    # Jika tidak ada pembagi selain 1 dan n, maka n adalah bilangan prima
    print("Bilangan Prima")

# Meminta pengguna memasukkan sebuah bilangan bulat
try:
    angka = int(input("Masukkan sebuah bilangan bulat: "))
    apakah_prima(angka)
except ValueError:
    print("Input tidak valid. Harap masukkan bilangan bulat.")
  
