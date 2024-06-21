# Program untuk mengkonversi suhu antara Celsius dan Fahrenheit

def celsius_ke_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_ke_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def menu():
    print("Konversi Suhu")
    print("1. Celsius ke Fahrenheit")
    print("2. Fahrenheit ke Celsius")
    print("3. Keluar")

def main():
    while True:
        menu()
        pilihan = input("Pilih opsi (1/2/3): ")

        if pilihan == '1':
            celsius = float(input("Masukkan suhu dalam Celsius: "))
            fahrenheit = celsius_ke_fahrenheit(celsius)
            print(f"{celsius}°C = {fahrenheit}°F\n")
        
        elif pilihan == '2':
            fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
            celsius = fahrenheit_ke_celsius(fahrenheit)
            print(f"{fahrenheit}°F = {celsius}°C\n")
        
        elif pilihan == '3':
            print("Keluar dari program.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan pilih opsi yang tersedia.\n")

if __name__ == "__main__":
    main()
  
