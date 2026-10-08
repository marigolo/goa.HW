# >
num = 15
num1 = num > 10
print(num1)

num2 = 44
num3 = num2 > 34
print(num3)


# <
num4 = 99
num5 = num4 < 130
print(num5)

num6 = 100
num7 = num6 < 450
print(num7)


# <=
num8 = 99
num9 = num8 <= 100
print (num9)

num10 = 68
num11 = num10 <= 68


# >=
num12 = 44
num13 = num12 >= 21
print(num13)

num14 = 69
num15 = num14 >= 69
print(num15)


# ==
num16 = 33
num17 = num16 == 33
print(num17)

num18 = 89
num19 = num18 == 89
print(num19)


# !=
num20 = 77
num21 = num20 != 77
print(num21)

num22 = 63 
num23 = num22 != 85
print(num23)



#or
num24 = True or False
print(num24)

num25 = False or True 
print(num25)

num26 = True or True
print(True)

num27 = False or False
print(num27)


#and
num28 = True and False
print(num28)

num29 = False and True 
print(num29)

num30 = True and True
print(num30)

num31 = False and False
print(num31)



height1 = float(input("enter your height "))
height2 = 1.53
num32 = height1 >= height2
print(num32)



num_1 = "21"
num_2 = 21
print(num1 == num2)
#გამოიტანს False რადგან: == ოპერატორი ამოჭმებს მონაცემების ტიპებსაც, ანუ რადგან num_1 str-ია ხოლო num_2 int-ია 
#ისინი არა არიან ერთმანეთის ტოლები მიუხედავად იმისა რომ მათი რიცხვითი მნიშვნელობა ტოლია.



surname = input("enter your surname ")
surname1 ="Goloshvili"
surname2 = surname == surname1
print(surname2)



num_3 = False or True and True and False
print(num_3)
#გამოიტანს False რადგან: True and True = True , True and False = False , False or False = False


num_4 = True and False or False or True
print(num_4)
# გამოიტანს True რადგან: True and False = False , False or False = False , False or True = True


num_5 = True or True and False or True or False and True or False
print(num_5)
# გამოიტანს True რადგან: True and False = False , False and True = False , False or True = True , False or True = True , True or Folse = True True or False = True




temp = int(input("enter temperature of your house "))
temp3 =  (temp and 30) and (temp > 30)
print(temp3)


 

temperature = float(input("enter the temperature in C "))
tem = (temperature * 1.8 ) + 32
temp4 = 89.6
temp5 = temp4 < tem
print(temp5)


