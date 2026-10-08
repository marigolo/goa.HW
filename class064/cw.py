# Multiple Inheritance - A(b, c)



class Teacher:
    def teach(self):
        print('Teaching')


class Researcher:
    def research(self):
        print('Researching')


class Professor(Teacher, Researcher):
    pass



# Multilevel Inheritance 

class Grandfather:
    def house(self):
        print("Has a house")


class Father(Grandfather):
    def car(self):
        print("Has a car")


class Son(Father):
    def bike(self):
        print("Has a bike")


son = Son()

son.house()
son.car()
son.bike()




''' CW '''


class Gadgets:
    def __init__(self, brand):
        self.brand = brand

    def info(self):
        print('This is a Gadget')


class Phone(Gadgets):
    def __init__(self, brand, model, price):
        super().__init__(brand)
        self.model = model
        self.price = price

    def call(self):
        print('Calling')


class Ios(Phone):
    pass


class Android(Phone):
    pass


phone1 = Ios('Apple', 'iPhone 13', 4005)

phone1.info()
phone1.call()

print(phone1.brand)
print(phone1.model)
print(phone1.price)



class VacuumCleaner:
    def Vacuum(self):
        print('Vacuuming')


class Robot:
    def DetectObstacle(self):
        print('Obstacle detected')


class RobotVacuum(VacuumCleaner, Robot):
    pass


robot = RobotVacuum()

robot.Vacuum()
robot.DetectObstacle()