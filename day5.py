import math

# Meminta pengguna memasukkan jari-jari lingkaran
radius = input("Masukkan jari-jari lingkaran: ")

# Memastikan input adalah angka dan mengonversi ke tipe float
try:
    radius = float(radius)
    if radius < 0:
        print("Jari-jari tidak boleh negatif.")
    else:
        # Menghitung luas lingkaran
        luas_lingkaran = math.pi * radius ** 2
        print(f"Luas lingkaran dengan jari-jari {radius} adalah: {luas_lingkaran}")
except ValueError:
    print("Input tidak valid. Harap masukkan angka.")
  
