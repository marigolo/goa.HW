'''
    2) Data Hiding არის ობიექტის შიგნით არსებული მონაცემების პირდაპირი წვდომისგან დაფარვა. 
    მისი მიზანია, რომ მონაცემები შემთხვევით ან არასწორად არ შეიცვალოს და მათზე წვდომა კონტროლირებული იყოს.
    მაგალითად, Data Hiding გამოგვადგება:
    - მომხმარებლის პაროლის დასაცავად;
    - საბანკო ანგარიშის ბალანსის დასამალად;
    - პირადი ინფორმაციის დასაფარად;
    - კლასის ისეთი მონაცემების დასაცავად, რომელთა პირდაპირ შეცვლაც არ გვინდა.
'''

class User:
    def __init__(self, password):
        self._password = password

info1 = User('12fg345')
        
        
# 3) Level 1 Data Hiding ხდება ატრიბუტის წინ ერთი _ - ის დაწერა.

class Person:
    def __init__(self, name):
        self._name = name
        
user = Person('maddy')
print(user._name)


# 4) Level 2 Data Hiding გამოიყენება ორი __-ის საშუალებით.

class   Paswrds:
    def __init__(self, password):
        self.__password = password
        
    def get_pass(self):
        return self.__password
        
info3 = Paswrds('uhuuh234')

        
print(info3.get_pass())

'''
    5)Encapsulation არის პრინციპი, როდესაც მონაცემებსა და მათზე მოქმედ ფუნქციებს ერთ 
    კლასში ვაერთიანებთ და საჭირო მონაცემებს გარედან პირდაპირი წვდომისგან ვიცავთ.
    მაგალითად, თუ Bank კლასში გვაქვს balance, შეგვიძლია მისი პირდაპირ შეცვლის ნაცვლად 
    გამოვიყენოთ მეთოდი, რომელიც ბალანსს უსაფრთხოდ შეცვლის.
'''

'''
    6) Name Mangling არის Python-ის მექანიზმი, რომელიც __-ით
    დაწყებულ ატრიბუტს ავტომატურად უცვლის შიდა სახელს.
    იგი გვჭირდება Level 2 Data Hiding-ის დროს, როდესაც გვინდა
    ატრიბუტზე პირდაპირი წვდომა უფრო მეტად შევზღუდოთ.
'''

# 7) UserInfo

class UserInfo:
    def __init__(self, name, surname, age, address):
        self.name = name
        self.surname = surname
        self._age = age
        self._address = address

    def get_age(self):
        return self._age

    def get_address(self):
        return self._address


user = UserInfo("Nika", "Beridze", 18, "Tbilisi")

# პირველი გზა
print(user._age)
print(user._address)

# მეორე გზა
print(user.get_age())
print(user.get_address())


# 8)

class Bank:
    def __init__(self, account_name, balance):
        self._account_name = account_name
        self.__balance = balance

    def get_account_name(self):
        return self._account_name


bank = Bank("Nika", 5000)

# account_name — ფუნქციის საშუალებით
print(bank.get_account_name())

# balance — name mangling-ით
# print(bank._Bank__balance)


# 9) 

class Book:
    def __init__(self, author, bookName, pageAmount):
        self._author = author
        self.__pageAmount = pageAmount

    def get_pageAmount(self):
        return self.__pageAmount

    def __display_pages(self):
        return self.__pageAmount


book = Book("J.K. Rowling", "Harry Potter", 300)

# author — კლასის გარედან, მეთოდის გარეშე
print(book._author)

# pageAmount — მეთოდის საშუალებით
print(book.get_pageAmount())

# pageAmount — name mangling-ით
# print(book._Book__pageAmount)

# display_pages — Private მეთოდის name mangling-ით
# print(book._Book__display_pages())