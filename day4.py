# Program untuk menerima input nomor HP dan memprosesnya

# Meminta pengguna memasukkan nomor HP
nomor_hp = input("Masukkan nomor HP Anda: ")

# Memastikan inputan hanya berisi angka
if nomor_hp.isdigit():
    # Mengubah input menjadi integer
    nomor_hp = int(nomor_hp)
    print("Nomor HP Anda adalah:", nomor_hp)
    print("Tipe data dari nomor HP:", type(nomor_hp))
else:
    print("Nomor HP yang dimasukkan tidak valid. Harus hanya berisi angka.")

# Contoh tambahan: Memisahkan kode negara dan nomor lokal
# Misalnya, jika nomor HP dalam format internasional (misal: +6281234567890)
nomor_hp_international = input("Masukkan nomor HP internasional Anda (misal: +6281234567890): ")

# Memastikan inputan memiliki tanda +
if nomor_hp_international.startswith('+') and nomor_hp_international[1:].isdigit():
    kode_negara = nomor_hp_international[1:3]  # Mengambil kode negara, misal +62
    nomor_lokal = nomor_hp_international[3:]   # Mengambil sisa nomor
    print("Kode Negara:", kode_negara)
    print("Nomor Lokal:", nomor_lokal)
else:
    print("Nomor HP internasional yang dimasukkan tidak valid.")
  
