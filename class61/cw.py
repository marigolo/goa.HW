'''
oop - objact oriented programing

blueprint - წესები რის მიხედვითაც ვქმნით გეგმა (class)

instance - objacts
atribut - objacts-ის გამანსხვავებელი ნიშანი

__init__ ინიციალიძაცია თავიდან შექმნა ისეთი რამის რაც არ არსებობს

self -  ამას ვიყენებთ იმისთვის რო გავიგოთ რომელ ინსტანციაზეა საუბარი, იგი აუცილებელია,  და არ არის ატრიბუტი
'''
# კლასი

class Car:
    def __init__(self, brand, model, color): #method
        self.brand = brand
        self.model = model
        self.color = color
    def honk(self):
        print(f'{self.brand}{self.model} is honking')
        
my_car = Car('BMW', 'M4', 'Black')

print(my_car.brand) #function
my_car.honk()
print(my_car.model) #function
print(my_car.color) #function




# ------------- CW ----------------------------


class Cat:
    def __init__(self, color, breed):
        self.color = color
        self.breed = breed
    def make_sound(self):
        print('Meow')
        
        
my_cat1 = Cat('white', 'Shorthair ')
my_cat2 = Cat('black', 'Persian ')

print(my_cat1.color)
print(my_cat1.breed)
my_cat1.make_sound()
print(my_cat2.color)
print(my_cat2.breed)
my_cat2.make_sound()


class Iphone:
    def __init__(self, model, price, color):
        self.model = model
        self.price = price
        self.color = color
    def pay(self):
        print(f'Succesfully paid {self.price} dollars to buy {self.model} price')
        

my_iphone1 = Iphone ('iphone18pro', '1500$', 'white')
my_iphone2 = Iphone ('iphone18promax', '6000$' ,'blue')


print(my_iphone1.model)
print(my_iphone1.price)
print(my_iphone1.color)
my_iphone1.pay()


print(my_iphone2.model)
print(my_iphone2.price)
print(my_iphone2.color)
my_iphone2.pay()