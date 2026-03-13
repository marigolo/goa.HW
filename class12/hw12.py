# 3) დაწერეთ პროგრამა, რომელიც ამოწმებს input-ით შემოყვანილი რიცხვი ლუწია თუ კენტი.
number = int(input("Enter a number "))
if number % 2 == 0:
   print("ლუწი")
else:
   print("კენტი")

# 4) დაწერეთ პროგრამა, რომელიც ამოწმებს ტემპერატურას:
# თუ > 30 -> "It's Hot"
# თუ 15-30 -> "It's Warm"
# თუ < 15 -> "It's Cold"

temp = float(input("what is the temperatur at home? "))
if temp > 30:
   print("Its hot")
elif temp >= 15:
   print( "It's Warm")
elif temp < 15:
   print("Its Cold")

# 5) მოხმარებელს შემოატანინეთ რიცხვი და დაბეჭდეთ:
# • "Positive even"
# • "Positive odd"
# • "Negative"

num1 = int(input("what is x: "))
if num1 % 2 == 0 and num1 > 0:
   print("Its possitive even")
elif num1 % 2 != 0 and num1 > 0:
   print("Its possitive odd")
elif num1 < 0:
   print("Its Negative ")

# 6) დაწერეთ პროგრამა რომელიც 0-დან მომხმარებლის შემოტანილ რიცხვამდე დაბეჭდავს:'Even' ან 'Odd'-ს
x = int(input("what is x? "))
if x % 2 == 0:
   print("Evan")
else:
   print("Odd")

# 7) მომხმარებელს შემოატანინეთ 10 რიცხვი. დაითვალეთ: რამდენია დადებითი, რამდენი უარყოფითი და ნული.
positive = 0
negative = 0
zero = 0

for i in range(10):
    num = int(input("შეიყვანე რიცხვი: "))

    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

print("positive numers:", positive)
print("negative numers:", negative)
print("zero:", zero)


# 8) მოცემულია სია:
# fruits = ["apple", "banana", "orange", "grape"]
# შეცვალეთ "banana" სიტყვა "kiwi"-ით და დაბეჭდეთ განახლებული სია.

fruits = ["apple", "banana", "orange", "grape"]
fruits = ["apple", "kivi", "orange", "grape"]
print(fruits [0], fruits [1], fruits [2], fruits [3])

# 9) მოცემულია სია:
# nums = [4, 8, 12, 16, 20]
# დაწერეთ პროგრამა, რომელიც:
# შეკრებს პირველ და ბოლო ელემენტს და დაბეჭდავს შედეგს.

nums = [4, 8, 12, 16, 20]
print(nums[0] + nums[-1])

# 10) შექმენით სია და დაპრინტე თითოეული წევრი.
cities = ["Tbilisi", "Tokio", "Berlin", "Paris"]
print(cities[0])
print(cities[1])
print(cities[2])
print(cities[3])
# 11) შექმენით რიცხვების სია დაპრინტე მხოლოდ ლუწი რიცხვები. 
x = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8]
print(x[1])
print(x[3])
print(x[5])
print(x[7])
# 12) შექმენით რიცხვების სია და დაპრინტე მხოლოდ ლუწი რიცხვების ჯამი. 
y = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8]
print(y[1] + y[3] + y[5] + y[7])
# 13) შექმენით რიცხვების სია და დაპრინტეთ მხოლოდ ის რიცხვები რომელიც მეტია 6 ზე.
z = [7 , 8 , 9 , 10 ]
print(z[0] + z[1] + z[2] + z[3])
# 14) შექმენით ცვლადი სადაც შეინახავ ნებისმიერ სიტყვას და დაპრინტე თითოეული ასო. 
name = "mari"
print (name[0])
print (name[1])
print (name[2])
print (name[3])
# 15) შექმენით სია და დაპრინტე პირველი სამი წევრი. 
name1 = "mari"
print (name[0])
print (name[1])
print (name[2])