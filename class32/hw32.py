# 2)

#Tuple unpacking ეწოდება პროცესს როდესაც Tuple-ის ელემენტები ცალკეულ ცვლადებში ვინახავთ

me = ("Mari", 15)
name , age = me

numbers = (1, 2, 3, 4, 5)
first , *middle , last = numbers

fruits = ("Apple", "Banana", "Cherry", "Kiwi")
fruit1 , fruit2 , *fruit3= fruits
 
# 3)

# შეგვიზლია გამოვიყენოთ: count(), len(), min(), max(), startswith(), endswith()

# 4)

#არშეგვიძლია გამოვიყენოთ: append(),  insert(), pop()

# 5)

info = ('Mari', 'Goloshvili', 15, 1.56, '22march')
name , surname , age , height , birthday = info

# 6)

num = (1, 4.5, 4, 9 ,8.9, 8)
num1 , *rest = num

# 7)

fruits = ('Apple', 'Pomegranate', 'Cherry', 'Strawberry', 'Blueberry')
*fruit1, fruit2, fruit3 = fruits
# არაფერს გამოიტანს რადგან არ შეიძლება Asterisk თავში გამოყენება რადგან ის ნიშნავს ყველა დანარCენ ელემენტს