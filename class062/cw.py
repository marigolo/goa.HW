'''
-------------- info --------------
inheritence - არის მემკვიდრეობა 

1 - იწერება perant class-ის
2) შვილს ()- ში ვუწერთ მშობელ კლასს

super() - მეთოდეს დახმარებით მშობლისგან გადმოდის არგუმენტად მითითებული თვისებები მშობლიდან შვილში  

3)შვილში
4) თუ გვინდა რომ შვილს დავუმატოთ ახალი ატრიბუტი 
მას თავიდან ვაცხადებთ
    
    
------------ method ------------
1) თუ გვინდა რომ მშობლის method ზუსტად გადმოვიტანოთ შვილში ვიყენებთ super().make_sound()

2)ხოლო თუ სხვა გვინდა  super()-ის წავშლით და დავწერთ     
def make_sound(self):
        return "mew"
'''


# class Animal:
#     def __init__(self, name, breed, color):
#         self.name = name
#         self.breed = breed
#         self.color = color

#     def make_sound(self):
#         return "making sound"


# class Cat(Animal):
#     def __init__(self, name, breed, color):
#         super().__init__(name, breed, color)

#     def make_sound(self):
#         return "mew" # ეწოდება Polymorphism


# cat1 = Cat("miki", "british", "white")

# print(cat1.make_sound())


# print(cat1.name)
# print(cat1.breed)
# print(cat1.color)


# -------------- CW --------------


'''
1) შექმენით Person კლასი (name, age).
შემდეგ შექმენით Student კლასი, რომელიც ამატებს grade-ს და super()-ით ინიციალიზაციას აკეთებს.

2) შექმენით Shape კლასი area() მეთოდით რომელიც დააბრუნებს საწყისად 0-ს (return 0).
შემდეგ შექმენით Rectangle კლასი (width, height), რომელიც super()-ს გამოიყენებს და მოახდენს area() მეთოდის override-ს.
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade


study = Student('lizzi', 18, 70)
study2 = Student('Anna', 20, 100)

print(study.name, study.age, study.grade)
print(study2.name, study2.age, study2.grade)


class Shape:
    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


rectangle = Rectangle(5, 10)
print(rectangle.area())