         #  0         1         2
cities = ["london", "tbilis","paris"]
            #  -3         -2      -1
print(cities[2])
print(cities[-1])

age = int(input("enter your age "))
if age < 12:
   print("child")
elif 12<= age < 18:
   print("teen")
elif age <= 100:
   # print("invalid age")
   for i in range(1, 100):
      print(i)
else:
   print("adult")

print("dont enter")


age = int(input("how old are you"))
if age < 18:
   is_student = bool(int(input("are you a student? {0-no/1-yes}: ")))
   if is_student:
      print("20% discaunt")
   else:
      print("10% discaunt")
else:
   print("regular praic")



# მატრიცა - სიაში სია
# ინდექსინგი არის როცა list-ში რომელიმე ელემენტს ვწვდეით

colors=["black", "red", "blue"]
for color in colors:
   print(f"my fav{color}")


num = int(input("enter numer"))
if num > 0:
   print("positive")
elif num < 0:
   print("negative")
else:
   print("zero")





fruits =["banana" , "apple" , "orange" , "mango" , "cherry"]
print(fruits[1])
print(fruits[2])
print(fruits[4])




password = "1233"
while True:
   n_password = input("enter password ")
   if password == n_password:
      print("you enterd")
      break
   else:      
      print("wrong try again")



# fruits = ["apple", "banana", "orange", "grape"]
fruits = ["apple", "kivi", "orange", "grape"]
print(fruits [0], fruits [1], fruits [2], fruits [3])
