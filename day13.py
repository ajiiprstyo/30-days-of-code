# Inputan Belanja
jumlah_barang = int(input('Masukkan jumlah barang : '))
harga_barang = int(input('Masukkan harga barang : '))
total_harga = jumlah_barang * harga_barang

# Menulis ke file invoice.txt dengan 'with' untuk penutupan otomatis
with open('invoice.txt', 'w') as file:
    file.write('------------RINCIAN------------\n')
    file.write(f'Jumlah Barang : {jumlah_barang}\n')
    file.write(f'Harga Barang  : Rp. {harga_barang:,.2f}\n')
    file.write('\n')
    file.write(f'TOTAL         : Rp. {total_harga:,.2f}\n')

# Mencetak ke layar
print()
print('------------RINCIAN------------')
print(f'Jumlah Barang : {jumlah_barang}')
print(f'Harga Barang  : Rp. {harga_barang:,.2f}')
print()
print(f'TOTAL         : Rp. {total_harga:,.2f}')
