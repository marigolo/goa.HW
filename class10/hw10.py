for i in range(50, 200 ):
   print(i)
print("პირველი დავალება END")

for i in range(2, 102, 2):
   print(i)
print("მეორე დავალება END")

for i in range(101, 151, 2):
    print(i)
print("მესამე დავალება END")

num = 1
while num <= 50:
    print(num)
    num += 1

num = 20
while num <= 60:
    print(num)
    num += 5

surname = input("enter your lastname ")
for i in surname:
    print(i)

juice = 300
while juice > 0:
    print("You have bought the drink!! there is" , juice ,"drink left" )
    juice -= 2
print("Out of stock")

for i in range(50, 20, -3):
    print(i)

num1 = 150
while num1 > 0:
    print(num1)
    num1 -= 1

#for loop ციკლი ვიყენებთ მაშინ როცა ვიცით რა და რამდენჯერ უნდა გამოვითანოთ ტერმინალში მას ტერმინალში გამოაქვს რიცხვები 
# start დან stop-ამდე კონკრეტული რიცხვის გამოტოვებით რომელიც შეგვიძლია მივუთითოთ

#while loop ციკლს ვიყენებთ როცა არ ვიცით რა ან რამდენჯერ უნდა გამოვითანოთ ტერმინალში 
# მას ტერმინალში გამოაქვს ინფორმაცია იქამდე სანამ პირობა სიმართლეა Counter საჭროა
#იმისათვის რომ გავიგოთ რამდენჯერ უნდა გამოვიტანოთ ტერმინალში ინფორმაცია
#Counter-ის მნიშვნელობის განახლება აუცილებელია რადგან მას თუ არ განვაახლებთ ციკლი არ დამთავრდება