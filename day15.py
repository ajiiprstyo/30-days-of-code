# Program Konversi Mata Uang Dollar ke Rupiah

# Nilai tukar Dollar ke Rupiah (sesuaikan dengan nilai tukar saat ini)
nilai_tukar = 14400  # Misalkan 1 USD = 14,400 IDR

def konversi_usd_ke_idr(dollar):
    """Fungsi ini mengkonversi nilai Dollar ke Rupiah"""
    return dollar * nilai_tukar

def main():
    try:
        usd = float(input("Masukkan jumlah Dollar (USD): "))
        idr = konversi_usd_ke_idr(usd)
        print(f"{usd} Dollar = Rp {idr:.2f} Rupiah")
    except ValueError:
        print("Input tidak valid. Silakan masukkan nilai numerik.")

if __name__ == "__main__":
    main()
