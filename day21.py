# Definisi Kelas Kontak
class Kontak:
    def __init__(self, nama, nomor_telepon, email):
        self.nama = nama
        self.nomor_telepon = nomor_telepon
        self.email = email

    def __str__(self):
        return f"Nama: {self.nama}, Nomor Telepon: {self.nomor_telepon}, Email: {self.email}"

# Definisi Kelas Buku Kontak
class BukuKontak:
    def __init__(self):
        self.kontak_list = []

    def tambah_kontak(self, nama, nomor_telepon, email):
        kontak = Kontak(nama, nomor_telepon, email)
        self.kontak_list.append(kontak)
        print("Kontak berhasil ditambahkan.")

    def lihat_kontak(self):
        if not self.kontak_list:
            print("Buku kontak kosong.")
        else:
            for idx, kontak in enumerate(self.kontak_list):
                print(f"{idx + 1}. {kontak}")

    def hapus_kontak(self, nama):
        for kontak in self.kontak_list:
            if kontak.nama.lower() == nama.lower():
                self.kontak_list.remove(kontak)
                print(f"Kontak dengan nama {nama} berhasil dihapus.")
                return
        print(f"Kontak dengan nama {nama} tidak ditemukan.")

# Fungsi utama untuk menjalankan program
def main():
    buku_kontak = BukuKontak()

    while True:
        print("\n--- Menu Buku Kontak ---")
        print("1. Tambah Kontak")
        print("2. Lihat Kontak")
        print("3. Hapus Kontak")
        print("4. Keluar")
        
        pilihan = input("Pilih opsi (1/2/3/4): ")

        if pilihan == '1':
            nama = input("Masukkan nama: ")
            nomor_telepon = input("Masukkan nomor telepon: ")
            email = input("Masukkan email: ")
            buku_kontak.tambah_kontak(nama, nomor_telepon, email)
        
        elif pilihan == '2':
            buku_kontak.lihat_kontak()
        
        elif pilihan == '3':
            nama = input("Masukkan nama kontak yang akan dihapus: ")
            buku_kontak.hapus_kontak(nama)
        
        elif pilihan == '4':
            print("Terima kasih telah menggunakan buku kontak!")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih opsi yang tersedia.")

if __name__ == "__main__":
    main()
              
