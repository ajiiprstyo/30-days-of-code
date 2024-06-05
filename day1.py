def konversi_km_ke_meter(kilometer):
    # 1 kilometer = 1000 meter
    meter = kilometer * 1000
    return meter

# Meminta input dari pengguna
kilometer = float(input("Masukkan jarak dalam kilometer: "))

# Melakukan konversi
meter = konversi_km_ke_meter(kilometer)

# Menampilkan hasil
print(f"{kilometer} kilometer sama dengan {meter} meter")
