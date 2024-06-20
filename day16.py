# Membuat kelas Hewan
class Hewan:
    def bersuara(self):
        pass

# Membuat kelas Kucing yang mewarisi kelas Hewan
class Kucing(Hewan):
    def bersuara(self):
        return "Meow"

# Membuat kelas Anjing yang mewarisi kelas Hewan
class Anjing(Hewan):
    def bersuara(self):
        return "Guk Guk"

# Membuat objek dan memanggil metode bersuara
hewan1 = Kucing()
hewan2 = Anjing()

print(hewan1.bersuara())
print(hewan2.bersuara())
