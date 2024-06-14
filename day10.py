class Item:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def checkout(self):
        total = sum([item.price for item in self.items])
        return total

def display_menu():
    print("\nMenu:")
    print("1. Barang Merah")
    print("2. Barang Putih")
    print("3. Barang Hijau")
    print("4. Checkout")
    print("5. Keluar")

# Membuat objek item
item1 = Item("Barang Merah", "Merah", 10000)
item2 = Item("Barang Putih", "Putih", 20000)
item3 = Item("Barang Hijau", "Hijau", 15000)

# Membuat keranjang
cart = Cart()

while True:
    display_menu()
    pilihan = int(input("Pilih menu (1-5): "))
    
    if pilihan == 1:
        cart.add_item(item1)
    elif pilihan == 2:
        cart.add_item(item2)
    elif pilihan == 3:
        cart.add_item(item3)
    elif pilihan == 4:
        total = cart.checkout()
        print("\nTotal tagihan: Rp", total)
    elif pilihan == 5:
        print("\nTerima kasih telah berbelanja!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
