class Tiket:
    def __init__(self, jumlah):
        self.jumlah = jumlah

    def hitung_harga(self):
        pass

class TiketBiasa(Tiket):
    def __init__(self, jumlah):
        super().__init__(jumlah)
        self.harga_per_tiket = 50000  # Harga tiket biasa

    def hitung_harga(self):
        return self.jumlah * self.harga_per_tiket

class TiketVIP(Tiket):
    def __init__(self, jumlah):
        super().__init__(jumlah)
        self.harga_per_tiket = 100000  # Harga tiket VIP

    def hitung_harga(self):
        return self.jumlah * self.harga_per_tiket

class TiketGold(Tiket):
    def __init__(self, jumlah):
        super().__init__(jumlah)
        self.harga_per_tiket = 150000  # Harga tiket Gold

    def hitung_harga(self):
        return self.jumlah * self.harga_per_tiket

def main():
    jenis_tiket = input("Masukkan jenis tiket (biasa/vip/gold): ").strip().lower()
    jumlah_tiket = int(input("Masukkan jumlah tiket: "))

    if jenis_tiket == 'biasa':
        tiket = TiketBiasa(jumlah_tiket)
    elif jenis_tiket == 'vip':
        tiket = TiketVIP(jumlah_tiket)
    elif jenis_tiket == 'gold':
        tiket = TiketGold(jumlah_tiket)
    else:
        print("Jenis tiket tidak valid.")
        return

    total_harga = tiket.hitung_harga()
    print(f"Total Harga Tiket: Rp {total_harga}")

if __name__ == "__main__":
    main()
  
