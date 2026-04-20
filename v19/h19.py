from turtle import *

bgcolor("#8DBDA9")

print("♡")

speed (10)
width = 3

penup()
goto(-250, -300)
pendown()

begin_fill()
color("#315437")
forward(500)
left(90)
left(0)
forward(300)
left(90)
forward(150)
right(90)
forward(180)
left(90)
forward(200)
left(90)
forward(180)
right(90)
forward(150)
left(90)
forward(300)
end_fill()

penup()
goto(120, 160)
right(135)
pendown()

begin_fill()
color("#3E5A49")
forward(170)
left(90)
forward(170)
end_fill()

penup()
goto(-255, 0)
pendown()

begin_fill()
color("#3E5A49")
right(135)
forward(40)
right(90)
forward(30)
right(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
left(90)
forward(20)
right(90)
forward(10)
end_fill()

penup()
goto(100, 0)
left(180)
pendown()

begin_fill()
color("#3E5A49")
right(0)
forward(40)
right(90)
forward(30)
right(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
left(90)
forward(10)
right(90)
forward(10)
end_fill()

penup()
goto(-60, 80)
pendown()

begin_fill()
color("#80B394")
circle(60)
end_fill()

penup()
goto(-25, 100)
pendown()

color("#D5DBD5")
right(90)
forward(25)
left(90)
forward(45)
left(90)
forward(30)
left(90)
forward(20)
left(90)
forward(15)


penup()
goto(-1, 63)
right(180)
pendown()

color("#080C08")
circle(17)

penup()
goto(15, 50)
left(65)
pendown()

color("#CAD2CA")
forward(60)
right(140)
forward(58)

penup()
goto(25, 70)
pendown()

color("#CAD2CA")
left(92)
forward(30)


penup()
goto(-100, -300)
left(73)
pendown()

begin_fill()
color("#8F806C")
forward(190)
right(90)
forward(200)
right(90)
forward(190)
end_fill()

exitonclick()




#1
name=input('enter your name: ')
surname=input('Enter your surname: ')
age=int(input('Enter your age: '))
place=input('Enter your place of living: ')
gender=input('Enter your gender: ')

print('Your name is ' + name + ' your age is '  + str(age) + ' u living in '+ place + ' your gender is '+ gender)
#ვიღებთ ინოფოტმაციას და ვპრინტავთ
#2
a=2
b=3
result_1= a+b
print(result_1)

a1=-1
b1=1
result_2=a1+b1
print(result_2)

a2=10
b2=20
result_3=a2 + b2  
print(result_3)
#ვქმნით ცვლადებს და ვასრულებთ მათემატიკურ ოპერაციებს

#3
number1=int(input('Enter number:'))
number2=int(input('Enter number:'))

x=number1 + number2
a=number1 - number2
y=number1 * number2
b=number1 / number2
c=number1 % number2
d=number1 // number2
print(x)
print(a)
print(y)
print(b)
print(c)
print(d)
#ვიღებთ 2 რიცხვს და ვასრულებთ მათემატიკურ ოპერაციებს

#4
a=2
b=3
c=4
result=a+b+c
print(result)

a1=-1
b1=1
c1=4
result1=a1+b1+c1
print(result1)

a2=5
b2=2
c2=2
result2=a2+b2+c2
print(result2)

#ვქმნით ცვლადებს და ვასრულებთ მათემატიკურ ოპერაციებს

#5
def this(a, b):

    if a == True and b == True:
        return a
    else:
        return b
print (this(7>0, 9>0))
#ვქმნით ფუნქციას  მასში თუ ორივე a და b ც მართასლია დაპრინტე სიმართლეა 

#6
def that(a, b):

    if a == False or b == True:
        return a
    else:
        return b

print (that(7<0, 9<0))
#ვქმნით ფუნქციას  მასში თუ ორივე a და bც მცდარია ან რომელიმე მცდარია  დაპრინტე სიცრუე 


#7
def is_even(nums):
    if nums % 2 == 0:
        return True
    else:
        return False

print (is_even(8))
#ვქმნით ფუნქციას  მასში თუ რიცხვი ლუწია  დაპრინტე სიმართლეა 

#8
def assa(a, b):

    if a > b:
        return True
    else:
        return False

print (assa(6, 9))
#ვქმნით ფუნქციას  მასში თუ ორივე a მეტია bზე  მართასლია დაპრინტე სიმართლეა 


#9

for i in range(0, 8):
    print(i)
    
#for ლუპით გამოპგვაქვს ციფრები სხვადასხვა ხაზზე 
    
#task10

i = 1
while i <= 5:
    print(i)
    i += 1
#while ლუპით ვამოწმებთ i > 5 და გამოგვაქ 

#task11

num = int(input('enter a number: '))
if num > 0:
    print('True')
else:
    print('False')
#ვქმნით ცვლადს ვიღებთ რიცხვს თუ 0> ვავრუნებთ სიმართლე
    
#task12

sum=0

for i in range(1,11):
    if i % 2==0:
        sum+=i
print(sum)

#for ლუპით 1-11მდე ვამოწმებთ ციფრები ლუწებს ვამატებთ


#extra1

list=[1,2,3]
result_4=len(list)
print(result)

list=[]
result_5=len(list)
print(result_5)
#ვამოწმებთ სიის სიგრძეს

#extra2

list = [3, 6, 8, 9]
result = max(list)
print(result)
#სიაში ვპოულობთ ყველაზე დიდ რიცხვს

#extra3

list = [1, 2, 5, 7]
result = 5 in list
print(result)
#ვამოწმებთ სიაში არის თუ არას 5

#extra4
def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b
    
print( max_of_two(1, 5))
#ვქმნით ფუნქციას სადაც თუ a მეტია b დავპრინტავთ a-ს

#extra5

def repeat_word(word, time):
    return word * time

print(repeat_word('hello' ,7 ))
#ვქმნით ფუნქციას სადაც სიტყვა გამოგვას იმდენჯერ რამდენიცა გვინდა


#6
def reverse_string(s):
   s = input('Enter word: ')
   return s[ : :-1]

print(reverse_string('s'))
print(reverse_string('s'))
#ვქმნით  ფუნქვიას სადაც სლაისინგით სიტყვას ვატრიალებთ

#7

weight=float(input('Enter your weight: '))
height=float(input('Enter your height: '))
def BMI(weight,height):
    x=weight/(height ** 2)
    if x > 30:
       print('Obese')
    elif 18.5 <= x < 25:
        print('Normal Weight')
    elif 25 <=x <30:
       print('Overweight')
    else:
        print('Underweight')

BMI(weight , height)
#შდემოვიტანეთ სიმაღლე და წონას ვითვლით BMI თუ >30 ვპრინტავთ Obese