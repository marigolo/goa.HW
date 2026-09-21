
# 3)

class Employees:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Managers(Employees):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
        

# 4)

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class Admin(User):
    def __init__(self, username, email, role):
        super().__init__(username, email)
        self.role = role
    
        
# 5)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
        
        
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
        self.salary = self.salary * 1.2
        print(self.salary)
        


# 7)

class Vehicle:
    def __init__(self, brand, year, color, horsePower):
        self.brand = brand
        self.year = year
        self.color = color
        self.horsePower = horsePower

    def drive(self):
        print(f'{self.color} {self.brand} is going')

    def stop(self):
        print(f'{self.color} {self.brand} is stopping')


class Car(Vehicle):
    def open_trunk(self):
        print(f'{self.brand} trunk is open')

    def honk(self):
        print(f'{self.brand} is honking')


class Motorcycle(Vehicle):
    def wheelie(self):
        print(f'{self.brand} is doing a wheelie')

    def start_engine(self):
        print(f'{self.brand} motorcycle engine started')


class Bike(Vehicle):
    def ring_bell(self):
        print(f'{self.brand} bell is ringing')

    def pedal(self):
        print(f'{self.brand} is being pedaled')


'''
2) 
Class Inheritance ნიშნავს, რომ შვილი კლასი  იღებს მშობელი კლასის თვისებებსა და მეთოდებს. 
ამის საშუალებით შეგვიძლია არსებული კოდის ხელახლა გამოყენება და შვილი კლასისთვის დამატებითი 
თვისებებისა და მეთოდების შექმნა.

8)
Multiple Inheritance — როდესაც ერთ შვილ კლასს ერთზე მეტი მშობელი კლასი ჰყავს.
Multilevel Inheritance — როდესაც მემკვიდრეობა რამდენიმე დონეზე გადადის:
'''