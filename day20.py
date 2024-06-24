# Kelas dasar (superclass)
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return "Some generic animal sound"

    def info(self):
        return f"Nama: {self.name}, Umur: {self.age} tahun"

# Kelas turunan (subclass) yang mewarisi dari kelas Animal
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # Memanggil konstruktor kelas dasar
        self.breed = breed

    def make_sound(self):
        return "Woof woof!"

    def info(self):
        # Memanggil info dari kelas dasar dan menambahkan informasi ras
        return super().info() + f", Ras: {self.breed}"

# Implementasi program
def main():
    # Membuat objek dari kelas Animal
    animal1 = Animal("Binatang", 5)
    print(animal1.info())
    print(f"Suara: {animal1.make_sound()}")
    
    # Membuat objek dari kelas Dog
    dog1 = Dog("Buddy", 3, "Golden Retriever")
    print(dog1.info())
    print(f"Suara: {dog1.make_sound()}")

if __name__ == "__main__":
    main()
  
