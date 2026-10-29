# 1) შექმენი Admin კლასი (username, email).
# შექმენი User კლასი, რომელიც ამატებს password-ს და super()-ით იძახებს მშობლის კონსტრუქტორს.

# 2) შექმენით MyInfo კლასი. მიანიჭეთ ატრიბუტები: name, age, address.
# პირველი დონის მონაცემთა დაფარვით - დაფარეთ age და address. შემდეგ გამოიძახეთ იგი როგორც name mangling-ით, ასევე კლასის მეთოდის დახმარებით.

# 3) შექმენი კლასი Apartment ატრიბუტებით address და price.
# კლასს ჰქონდეს ცვლადი მაგ. discount_rate = 0.0 (0%).
# დაწერე @classmethod სახელად set_discount_rate(cls, new_rate), რომელიც შეცვლის ფასდაკლების პროცენტს ყველა ბინისათვის.
# დაწერე ობიექტის მეთოდი get_discounted_price(), რომელიც დააბრუნებს ფასს ფასდაკლების გათვალისწინებით.


# 1)

class Admin:
    def __init__(self, username, email):
        self.username = username
        self.email = email


class User(Admin):
    def __init__(self, username, email, password):
        super().__init__(username, email)
        self.password = password


user1 = User("Nika", "nika@gmail.com", "12345")

print(user1.username)
print(user1.email)
print(user1.password)

# 2)

class MyInfo:
    def __init__(self, name, age, address):
        self.name = name
        self._age = age
        self._address = address

    def get_info(self):
        return self._age, self._address


person1 = MyInfo("Nika", 18, "Tbilisi")

# ატრიბუტებზე წვდომა name mangling-ის გარეშე
print(person1.name)
print(person1._age)
print(person1._address)

# კლასის მეთოდის დახმარებით
print(person1.get_info())

# 3)

class MyInfos:
    def __init__(self, name, age, address):
        self.name = name
        self.__age = age
        self.__address = address

    def get_info(self):
        return self.__age, self.__address


person1 = MyInfos("Nika", 18, "Tbilisi")

# Name mangling-ით
print(person1._MyInfos__age)
print(person1._MyInfos__address)

# კლასის მეთოდის დახმარებით
print(person1.get_info())