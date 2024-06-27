import random
import string

def generate_password(length):
    if length < 4:
        print("Panjang kata sandi harus minimal 4 karakter.")
        return None
    
    # Menggabungkan semua karakter yang mungkin digunakan dalam kata sandi
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Memastikan setidaknya satu huruf besar, huruf kecil, angka, dan simbol dalam kata sandi
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    # Mengisi sisa kata sandi dengan karakter acak dari semua_characters
    password += random.choices(all_characters, k=length-4)
    
    # Mengacak urutan karakter dalam kata sandi
    random.shuffle(password)
    
    return ''.join(password)

def main():
    try:
        length = int(input("Masukkan panjang kata sandi yang diinginkan: "))
        password = generate_password(length)
        if password:
            print(f"Kata sandi acak Anda: {password}")
    except ValueError:
        print("Masukkan panjang yang valid.")

if __name__ == "__main__":
    main()
          
