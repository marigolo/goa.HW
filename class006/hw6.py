#2)type ფუნქციას ტერმინალში გამოაქვს თუ რა ტიპისაა მასში შეტანილი მონაცემი

#2.1.
age1 = type(15)
name1 = type("mari")
surname1 = type("goloshvli")
man = type(False)
Woman = type(True) 
print(age1)
print(name1)
print(surname1)
print(man)
print(Woman)

#3)
#3.1
name = "mari"
surname = "goloshvili"
age = 15
print("my name is", name, surname, "and i am", age, "years old")

#3.2
name = "mari "
surname = "goloshvili "
age = "15"
about_me = "my name is " + name + surname +"and i am " + age + " years old"
print(about_me)

#4)
num1 = float(input("enter first number "))
num2 = float(input("enter second number "))
add = num1 + num2
print(add)
minuse = num1 - num2
print(minuse)
times = num1 * num2
print(times)
divaid = num1 / num2
print(divaid)

#5)
num3 = int(input("enter 1st number "))
num4 = int(input("enter 2nd number "))
num5 = int(input("enter 3th number "))
num6 = int(input("enter 4t number "))
num7 = int(input("enter 5th number "))
everge = num3 + num4 + num5 + num6 + num7
print(everge / 5)

#6)
temperature = float(input("enter the temperature in C "))
tem = temperature * 1.8 + 32
print(tem)

#7)
temperature2 = float(input("enter the temperature in F "))
tem2 = temperature2 - 32
formul2 = tem2 / 1.8
print(formul2)