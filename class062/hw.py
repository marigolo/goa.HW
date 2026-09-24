# 3)

class Employees:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Managers(Employees):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
        
manager = Managers("Nika", 3000, "IT")

print(manager.name)
print(manager.salary)
print(manager.department)

# 4)

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class Admin(User):
    def __init__(self, username, email, role):
        super().__init__(username, email)
        self.role = role
    
admin = Admin("mari", "mari@gmail.com", "Administrator")

print(admin.username)
print(admin.email)
print(admin.role)
   
# 5)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
 
        
        
book = EBook("Harry Potter", "J.K. Rowling", 25)

print(book.title)
print(book.author)
print(book.file_size)


# 6)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        print(self.salary)


class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def bonus_salary(self):
        s = self.salary = self.salary * 0.2
        print(s)
        
# შექმენით მშობელი კლასი Vehicle. მიეცით მას თვისებები: brand, year, color, horsePower. მშობელ კლასში დაამატეთ drive() მეთოდი, რომელიც დაბეჭდავს '{color} {brand} is going'. ასევე შექმენით stop() მეთოდი, რომელიც დაბეჭდავს '{color} {brand} is stopping'. შექმენით child კლასები: Car, Motorcycle, Bike. გადაეცით შვილ კლასებს მშობლის თვისებები და მეთოდები. ამასთანავე თქვენი ფანტაზიით მოიფიქრეთ და დაამატეთ სხვადასხვა მეთოდები შვილ კლასებში.

# 7)

class Vehicle:
    def __init__(self, brand, year, color, horsePower):
        self.brand = brand
        self.year = year
        self.color = color
        self.horsePower = horsePower

    def drive(self):
        print(f"{self.color} {self.brand} is going")

    def stop(self):
        print(f"{self.color} {self.brand} is stopping")


class Car(Vehicle):
    def __init__(self, brand, year, color, horsePower):
        super().__init__(brand, year, color, horsePower)
    def open_trunk(self):
        print(f"{self.brand} trunk is open")


class Motorcycle(Vehicle):
    def __init__(self, brand, year, color, horsePower):
        super().__init__(brand, year, color, horsePower)
    def wheelie(self):
        print(f"{self.brand} is doing a wheelie")


class Bike(Vehicle):
    def __init__(self, brand, year, color, horsePower):
        super().__init__(brand, year, color, horsePower)
    def ring_bell(self):
        print(f"{self.brand} bell is ringing")


car = Car("BMW", 2022, "Black", 250)
motorcycle = Motorcycle("Yamaha", 2023, "Blue", 120)
bike = Bike("Trek", 2024, "Red", 0)

car.drive()
car.open_trunk()

motorcycle.drive()
motorcycle.wheelie()

bike.drive()
bike.ring_bell()

'''
2) 
Class Inheritance ნიშნავს, რომ შვილი კლასი  იღებს მშობელი კლასის თვისებებსა და მეთოდებს. 
ამის საშუალებით შეგვიძლია არსებული კოდის ხელახლა გამოყენება და შვილი კლასისთვის დამატებითი 
თვისებებისა და მეთოდების შექმნა.

8)
Multiple Inheritance — როდესაც ერთ შვილ კლასს ერთზე მეტი მშობელი კლასი ჰყავს.
Multilevel Inheritance — როდესაც მემკვიდრეობა რამდენიმე დონეზე გადადის:
'''