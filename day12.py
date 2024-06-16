class Employee:
    def __init__(self, name="", age=0, salary=0.0):
        self.__name = name
        self.__age = age
        self.__salary = salary

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

# Membuat object berdasarkan class Employee
employee = Employee()

# Mengimplementasikan semua method yang ada
employee.set_name("Aji Prasetyo")
employee.set_age(19)
employee.set_salary(50000)

print("Employee Name:", employee.get_name())
print("Employee Age:", employee.get_age())
print("Employee Salary:", employee.get_salary())
