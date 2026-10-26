'''
2) შექმენი კლასი Student, რომელსაც ექნება ატრიბუტები name და age. შექმენი კლასის ცვლადი total_students = 0. ყოველ ჯერზე, როდესაც ახალი სტუდენტი შეიქმნება (__init__), total_students უნდა გაიზარდოს 1-ით.

3) შექმენი კლასი Book ატრიბუტებით: title, author, year. დაწერე @classmethod სახელად from_string, რომელიც მიიღებს სტრიქონს ფორმატით: "Title - Author - Year" (მაგალითად: "1984 - George Orwell - 1949"), დაშლის მას და დააბრუნებს Book კლასის ახალ ობიექტს.

4) შექმენი კლასი Temperature, რომლის __init__ ინახავს ტემპერატურას ცელსიუსში (celsius).
დაწერე @classmethod სახელად from_fahrenheit(cls, fahrenheit), რომელიც მიიღებს ტემპერატურას ფარენჰეიტში, გადაიყვანს ცელსიუსში (C = (F - 32) * 5/9) და დააბრუნებს Temperature-ის ახალ ობიექტს.

5) ექმენი კლასი Product ატრიბუტებით name და price.
კლასს ჰქონდეს ცვლადი discount_rate = 0.0 (0%).
დაწერე @classmethod სახელად set_discount_rate(cls, new_rate), რომელიც შეცვლის ფასდაკლების პროცენტს ყველა პროდუქტისთვის.
დაწერე ობიექტის მეთოდი get_discounted_price(), რომელიც დააბრუნებს ფასს ფასდაკლების გათვალისწინებით.

6) ექმენი კლასი MathUtils.
დაწერე @staticmethod სახელად is_even(number), რომელიც შეამოწმებს, არის თუ არა რიცხვი ლუწი (დააბრუნებს True ან False).
დაწერე მეორე @staticmethod სახელად factorial(n), რომელიც დააბრუნებს გადაცემული რიცხვის ფაქტორიალს.

7) შექმენი კლასი Validator.
დაწერე @staticmethod სახელად is_valid_email(email), რომელიც შეამოწმებს, შეიცავს თუ არა სტრინგი @ და . სიმბოლოებს და არ არის თუ არა ცარიელი. მეთოდმა უნდა დააბრუნოს True ან False.

8) ექმენი კლასი DateHelper.
დაწერე @staticmethod სახელად is_leap_year(year), რომელიც დაადგენს, არის თუ არა წელი ნაკიანი (ნაკიანია წელი, რომელიც იყოფა 4-ზე, მაგრამ არ იყოფა 100-ზე, გარდა იმ შემთხვევისა, როცა იყოფა 400-ზე).

9) შექმენი კლასი SecurityUtils.
დაწერე @staticmethod სახელად check_password_strength(password), რომელიც დააბრუნებს "Strong", თუ პაროლი არის მინიმუმ 8 სიმბოლო და შეიცავს როგორც ციფრებს, ასევე ასოებს. წინააღმდეგ შემთხვევაში დააბრუნებს "Weak".

10) შექმენი კლასი TextFormatter.
დაწერე @staticmethod სახელად clean_text(text), რომელიც ტექსტს ჩამოაცილებს ზედმეტ space-ებს დასაწყისსა და ბოლოში და ყველა ასოს გადაიყვანს lowercase-ში.
დაწერე @staticmethod სახელად count_words(text), რომელიც დააბრუნებს ტექსტში სიტყვების რაოდენობას.


'''


# 2)

class Student:
    total_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.total_students += 1


s1 = Student('Nika', 18)
s2 = Student('Mariam', 17)
s3 = Student('Giorgi', 19)

print(Student.total_students)


# 3)

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    @classmethod
    def from_string(cls, text):
        title, author, year = text.split(' - ')
        return cls(title, author, int(year))


book1 = Book.from_string('1984 - George Orwell - 1949')

print(book1.title)
print(book1.author)
print(book1.year)


# 4)

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        celsius = (fahrenheit - 32) * 5 / 9
        return cls(celsius)


temp = Temperature.from_fahrenheit(100)

print(round(temp.celsius, 2))


# 5)

class Product:
    discount_rate = 0.0

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def set_discount_rate(cls, new_rate):
        cls.discount_rate = new_rate

    def get_discounted_price(self):
        return self.price * (1 - Product.discount_rate / 100)


p1 = Product('Laptop', 2000)
p2 = Product('Phone', 1000)

Product.set_discount_rate(20)

print(p1.get_discounted_price())
print(p2.get_discounted_price())


# 6)

class MathUtils:
    def __init__(self):
        pass

    @staticmethod
    def is_even(number):
        return number % 2 == 0

    @staticmethod
    def factorial(n):
        result = 1

        for i in range(1, n + 1):
            result *= i

        return result


print(MathUtils.is_even(8))
print(MathUtils.is_even(5))
print(MathUtils.factorial(5))


# 7)

class Validator:
    def __init__(self):
        pass

    @staticmethod
    def is_valid_email(email):
        return email != '' and '@' in email and '.' in email


print(Validator.is_valid_email('test@gmail.com'))
print(Validator.is_valid_email('testgmailcom'))
print(Validator.is_valid_email(''))


# 8)

class DateHelper:
    def __init__(self):
        pass

    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


print(DateHelper.is_leap_year(2024))
print(DateHelper.is_leap_year(1900))
print(DateHelper.is_leap_year(2000))


# 9)

class SecurityUtils:
    def __init__(self):
        pass

    @staticmethod
    def check_password_strength(password):
        has_letter = any(char.isalpha() for char in password)
        has_digit = any(char.isdigit() for char in password)

        if len(password) >= 8 and has_letter and has_digit:
            return 'Strong'

        return 'Weak'


print(SecurityUtils.check_password_strength('Python123'))
print(SecurityUtils.check_password_strength('python'))
print(SecurityUtils.check_password_strength('12345678'))


# 10)


class TextFormatter:
    def __init__(self, text):
        self.text = text

    @staticmethod
    def clean_text(text):
        return text.strip().lower()

    @staticmethod
    def count_words(text):
        return len(text.split())


text1 = TextFormatter('   Hello World Python   ')

print(TextFormatter.clean_text(text1.text))
print(TextFormatter.count_words(text1.text))

