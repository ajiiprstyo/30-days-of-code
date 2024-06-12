# Fungsi untuk melakukan operasi perkalian
def perkalian(angka1, angka2):
    return angka1 * angka2

# Meminta pengguna memasukkan dua angka
try:
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    # Memanggil fungsi perkalian dan mencetak hasilnya
    hasil = perkalian(angka1, angka2)
    print(f"Hasil perkalian {angka1} dan {angka2} adalah {hasil}")
except ValueError:
    print("Input tidak valid. Harap masukkan angka.")
  
