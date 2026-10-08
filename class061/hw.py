# 1)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        return f'Hello, my name is {self.name} and I am {self.age} years old'
        
ME = Person('Mari', 15)
print(ME)
print(ME.introduce())


# 2)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)

rectangle = Rectangle(5, 3)

print('Area:', rectangle.area())
print('Perimeter:', rectangle.perimeter())


# 3)

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity


products = [Product('Apple', 2, 10), Product('Laptop', 1200, 2), Product('Book', 15, 5), Product('Phone', 800, 3)]

most_expensive = max(products, key=lambda product: product.price) 
#ვეუბნებით რომ აიღე ერთი product და დამიბრუნე მისი price. შემდეგ მათგან ვიღებთ ყველაზე დიდს
cheapest = min(products, key=lambda product: product.price)

print('ყველაზე ძვირი:', most_expensive.name, most_expensive.price)
print('ყველაზე იაფი:', cheapest.name, cheapest.price)


# 5)

class Dog:
    def __init__(self, breed, age, color):
        self.breed = breed
        self.age = age
        self.color = color

    def make_sound(self):
        return 'Woof!'

    def bark(self):
        return f'{self.age} years old {self.breed} is barking'


dog1 = Dog('German Shepherd', 3, 'Black')

print(dog1.breed)
print(dog1.age)
print(dog1.color)
print(dog1.make_sound())
dog1.bark()

dog2 = Dog('Labrador', 5, 'Golden')

print(dog2.breed)
print(dog2.age)
print(dog2.color)
print(dog2.make_sound())
dog2.bark()