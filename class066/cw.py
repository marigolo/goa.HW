'''
Date hiding - არის მთავარი იდია როცა  გვჭირდება რაიმე ინფორმაციის დაფარვა როგორიცაა პირადი ინფორმაცია

Date hiding-ს აქვს 2 level hiding-ის:
1 - შევქმნათ ატრიბუტუ _ -ი

გამოძახების ხერხები: 1.print(user1.display_Id()), 2.print(user1._password)

2 - შევქმნათ ატრიბუტუ __(2ცალი _ ) -ი 
გამოძახების ხერხები: 1.def display_I(self):return self._Id, 2.
level 2 = private

Ncapsulation - კლასის შიგნით ვწვდებით და გარედან ვერ გამოვიძახებთ

'''
# level 1
class Users:
    def __init__(self, name, usrename, Id):
        self.name = name
        self.usrename = usrename
        # დაიფარა level 1 data hiding
        self._Id = Id

    def display_Id(self):
        return self._Id


user1 = Users('ben', 'JJ', 1234455)

print(user1.name)
print(user1.usrename)
print(user1.display_Id())
print(user1._Id)


# lever 2

class CreditCard:
    def __init__(self, number, cvc, expDate):
        self.number = number
        self.expDate = expDate
        self.__cvc = cvc

    def dysplay_cvv(self):
        return self.__cvc


card1 = CreditCard(233453, 342, '09/24')

print(card1.dysplay_cvv())
# print(card1._CreditCard__cvc) 

# ............. CW ..............


# 1)

class Map:
    def __init__(self, country, IP_location, city):
        self.country = country
        self._IP_location = IP_location
        self.city = city
    def display_ip(self):
        return self._IP_location
    
map1 = Map('Georgia', '196.292.11', 'Tbilisi')
        
print(map1.display_ip())
print(map1._IP_location)


# 2)

class User:
    def __init__(self, name, usrename, email, password):
        self.name = name
        self.usrename = usrename
        self._email = email
        self._password = password

    def display_email(self):
        return self._email
    def display_password(self):
        return self._password


user1 = User('ben', 'JJ', 1234455, '123fg3')

print(user1.name)
print(user1.usrename)
print(user1.display_email())
print(user1._email)
print(user1.display_password())
print(user1._password)