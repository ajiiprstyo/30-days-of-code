class Mahasiswa:
    def __init__(self, nim, nama, angkatan, prodi):
        self.nim = nim
        self.nama = nama
        self.angkatan = angkatan
        self.prodi = prodi

    def kartu_mahasiswa(self):
        print(f"NIM: {self.nim}")
        print(f"Nama: {self.nama}")
        print(f"Angkatan: {self.angkatan}")
        print(f"Prodi: {self.prodi}")

    def selamat(self):
        print(f"Selamat datang {self.nama} di kampus UMS")


# Membuat minimal 3 objek dari class Mahasiswa
mahasiswa1 = Mahasiswa("A710230066", "Aji Prasetyo", 2023, "PTI")
mahasiswa2 = Mahasiswa("A710230064", "Jose", 2024, "PTI")
mahasiswa3 = Mahasiswa("A710230063", "Fahrul", 2023, "PTI")

# Memanggil method kartu_mahasiswa dan selamat untuk tiap objek
mahasiswa1.kartu_mahasiswa()
mahasiswa1.selamat()

mahasiswa2.kartu_mahasiswa()
mahasiswa2.selamat()

mahasiswa3.kartu_mahasiswa()
mahasiswa3.selamat()
