def tampilkan_menu():
    print("\n--- MENU TO-DO LIST ---")
    print("1. Lihat Semua Tugas")
    print("2. Tambah Tugas Baru")
    print("3. Hapus Tugas")
    print("4. Keluar")
    print("-----------------------")

def lihat_tugas(tugas):
    if not tugas:
        print("Tidak ada tugas dalam daftar.")
    else:
        print("\nDaftar Tugas:")
        for idx, task in enumerate(tugas, start=1):
            print(f"{idx}. {task}")

def tambah_tugas(tugas):
    tugas_baru = input("Masukkan tugas baru: ")
    tugas.append(tugas_baru)
    print(f"Tugas '{tugas_baru}' telah ditambahkan.")

def hapus_tugas(tugas):
    lihat_tugas(tugas)
    try:
        nomor_tugas = int(input("Masukkan nomor tugas yang akan dihapus: "))
        if 1 <= nomor_tugas <= len(tugas):
            tugas_terhapus = tugas.pop(nomor_tugas - 1)
            print(f"Tugas '{tugas_terhapus}' telah dihapus.")
        else:
            print("Nomor tugas tidak valid.")
    except ValueError:
        print("Input tidak valid. Masukkan nomor tugas yang benar.")

def main():
    tugas = []
    while True:
        tampilkan_menu()
        pilihan = input("Pilih opsi (1/2/3/4): ")
        
        if pilihan == '1':
            lihat_tugas(tugas)
        elif pilihan == '2':
            tambah_tugas(tugas)
        elif pilihan == '3':
            hapus_tugas(tugas)
        elif pilihan == '4':
            print("Terima kasih telah menggunakan aplikasi to-do list!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih opsi yang tersedia.")

if __name__ == "__main__":
    main()
  
