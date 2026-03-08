
for i in range(10):
   print("hello")

for i in range(10):
   print(i + 3)

for i in range(3,4,5):
   print(i)

for i in range(3 , 8, 2):
   print(f"Hello:{i}")

academy  = "goa 2"
for i in academy:
   print(i)

nu=4
while nu < 9:
   print(nu)
   nu=nu+1

nu=4
while nu < 9:
   print(nu)
   nu+=1

tikets = int(input("tikets"))
while tikets > 0:
   print("tikets have een sold")
   tikets -= 1
   print(f"{tikets} have left")

password ="1 2 3"
user_password = input("enter the password")
while password != user_password:
   print("wrong")
   user_password = input("enter the password")

print("you have loged in")

