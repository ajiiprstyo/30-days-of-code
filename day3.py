class TiketKeretaApi:
    def __init__(self, harga_dasar):
        self.harga_dasar = harga_dasar

    def hitung_diskon(self, umur):
        if umur < 5:
            return 100  # Diskon 100% untuk anak di bawah 5 tahun
        elif 5 <= umur <= 12:
            return 50  # Diskon 50% untuk anak usia 5-12 tahun
        elif umur >= 60:
            return 30  # Diskon 30% untuk lansia usia 60 tahun ke atas
        else:
            return 0  # Tidak ada diskon untuk lainnya

    def hitung_harga_akhir(self, diskon):
        return self.harga_dasar * (1 - diskon / 100)

def main():
    harga_dasar = float(input("Masukkan harga dasar tiket: "))
    tiket = TiketKeretaApi(harga_dasar)
    
    while True:
        input_umur = input("Masukkan umur penumpang (atau ketik 'selesai' untuk mengakhiri): ")
        
        if input_umur.lower() == 'selesai':
            break

        try:
            umur = int(input_umur)
        except ValueError:
            print("Input tidak valid. Harap masukkan umur dalam angka.")
            continue
        
        diskon = tiket.hitung_diskon(umur)
        harga_akhir = tiket.hitung_harga_akhir(diskon)

        print(f"Umur penumpang: {umur} tahun")
        print(f"Diskon: {diskon}%")
        print(f"Harga akhir tiket: Rp{harga_akhir:.2f}")
        print("-" * 30)

    print("Terima kasih telah menggunakan layanan kami.")

if __name__ == "__main__":
    main()
  
