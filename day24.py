def hitung_jumlah_kata(teks):
    teks = teks.strip()  # Menghapus spasi ekstra di awal dan akhir teks
    if not teks:
        return 0
    else:
        # Menggunakan split() untuk membagi teks berdasarkan spasi dan menghitung jumlah kata
        kata = teks.split()
        return len(kata)

def main():
    print("Program Penghitung Jumlah Kata")
    teks = input("Masukkan teks: ")
    jumlah_kata = hitung_jumlah_kata(teks)
    print(f"Jumlah kata dalam teks yang dimasukkan adalah: {jumlah_kata}")

if __name__ == "__main__":
    main()
  
