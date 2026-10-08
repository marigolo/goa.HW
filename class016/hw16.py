  
#   2) მომხმარებელს შემოატანინეთ 5 რიცხვი და ეტაპობრივად დაამატეთ ისინი სიაში. გამოთვალეთ სიაში შენახულ რიცხვთა საშუალო 
# არითმეტიკული 

num = []
for i in range(5):
    number = int(input(f'enter a number {i+1}: ')) 
    num.append(number)
average = sum(num) / len(num)

print('the Arithmetic mean of numbers you enterd is: ', average)

# 3) მომხმარებელს შემოატანინეთ წინადადება და ტერმინალში გამოიტანეთ მისი სიგრძე.

Phrase = input('enter a Phrase: ')
length = len(Phrase)
print(f'the lenght of Phrase you enterd is {length}')

# 4) მომხმარებლის შეინახეთ password ცვლადში. გამოიყენეთ find ფუნქცია და გაარკვიეთ მომხმარებლის 
# პაროლი შეიცავს თუ არა 1-იანს (სტრინგი უნდა იყოს).
# გამოიყენეთ if else-ები (hint: find-ის მიერ დაბრუნებული ინდექსი გამოიყენეთ if-else ში)

password = input('enter a password: ')
fineded = password.find('1')
if fineded != '-1':
    print('your password dosnot contain simble "1"')
else:
    print('your password contains simble "1"')
    
# 5) შექმენით fruits სია. სიის ბოლოში დაამატეთ 'cherry', სიიდან ამოშალეთ მესამე index-ზე მდგომი 
# ელემენტი და მის ნაცვლად (ე.ი მესამე ინდექსზე) დაამატეთ 'Blueberry'.

fruits = ['Strawberry', 'Banana', 'Dragon frute', 'Mango', 'Watermelon', 'Melon']
fruits.append('cherry')
fruits.pop(3)
fruits.insert(3, 'Blueberry')
print(fruits)

# 6) მომხმარებელს შემოატანინეთ სიტყვა. შეამოწმეთ არის თუ არა სიტყვის პირველი ასო დიდი. 
# თუ იქნება - გამოიტანეთ 'Perfect', თუ არ იქნება მაშინ გამოუტანეთ 'Your word should be capitalized!'

word = input('enter a word: ')
if word != word.capitalize():
    print('Your word should be capitalized!')
else:
    print('Perfect')

# 7) დაწერეთ პროგრამა, რომელიც მომხმარებლის მიერ შემოტანილ სახელსა და გვარს გადაიყვანს:
# • Uppercase
# • Lowecase

name = input('enter your name: ')
surname = input('enter your surname: ')
print(name.upper())
print(surname.upper())

name = input('enter your name: ')
surname = input('enter your surname: ')
print(name.lower())
print(surname.lower())

# 8) ცვლადში შეინახე შენი სახელი. მომხმარებელს შეეკითხე თავისი სახელი, იმ შემთხვევაში თუ თქვენი 
# სახელები ემთხვევა დაბეჭდეთ "Our names are similar!", თუ არ ემთხვევა დაბეჭდეთ "We have different names".
# გაითვალისწინეთ, რომ მომხმარებელმა შეიძლება თქვენნაირი სახელი შემოიტანოს, თუმცა სახელის ასოები შესაძლოა იყოს სხვადასხვა 
# შრიფტის ზომით, ამიტომ ამან თქვენ პროგრამაში შეფერხება არ უნდა გამოიწვიოს (გამოიყენეთ ნასწავლი სტრინგის მეთოდები)

Name = 'Mari'
Name_usur = input('enter your name please ')
usuar = Name_usur.capitalize()
if Name == usuar:
    print('Our names are similar!')
else:
    print('We have different names')


# 9) ცვლადში შეინახეთ რაიმე სტრინგი, შემდეგ .find() ფუნქციის მეშვეობით იპოვეთ რომელ ინდექსზეა კონკრეტული ასო.

string = 'Hello'
index = string.find('l')
print(f'in word Hello l is in {index} index')

# 10) შექმენით სია, სადაც დაამატებთ რანდენიმე სტრინგს. სიაში დამატებული თითოეული 
# სტრინგი გადაიყვანეთ დიდ ასოებად for ციკლის მეშვეობით.

names = ['Mari', 'Lizi', 'Lika', 'Barbare'] 
upper_case = []
for i in names:
    upper_case.append(i.upper()) 
print(upper_case)

# 11) შექმენით ცარიელი სია. მომხმარებელს 3-ჯერ შემოატანინეთ რაიმე მონაცემი და ყოველ 
# ჯერზე დაამატეთ ის სიაში append() ფუნქციით.
# ბოლოს დაბეჭდეთ სია.

lists = []
for i in range(3):
    NUm = int(input(f'enter number {i + 1}: '))
    lists.append(NUm)   
print(lists)
    
# 12) შექმენით Fruits სია 4 ელემენტით.
# მომხმარებელს შემოატანინეთ ახალი ხილი და ჩასვით ის სიის მეორე ინდექსზე.
# საბოლოოდ ტერმინალში გამოიტანეთ განახლებული სია.

Fruit = ['Apple', 'Dragon frutie', 'Mango', 'banana']
fruit = input('enter a Fruit: ')
Fruit.append(fruit)
print(Fruit)