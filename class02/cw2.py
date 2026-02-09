#1) კომენტარის სახით ახსენით ყველა მათემატიკური ოპერატორი და მოიყვანეთ თითოეულ ოპერატორზე ერთი მაგალითი და დაპრინტეთ 
#2) კომენტარის სახით ახსენით რა არის კონკატინაცია, მოიყვანეთ ორი მაგალითი და დაპრინტეთ 
#3) შექმენი ცვლადები num1 , num2 შეინახეთ integer ტიპის მნიშვნელობები და დაპრინტეთ მათი ჯამი 
#4) შექმენი ცვლადები name , age , height შეინახეთ შესაბამისი მნიშვნელობები და f string-ის გამოყენებით დაბეჭდეთ წინადადება 
#"Hello <name>, my age is <age> and my height is <height>"


# + ამატებს integer ტიპის ცვლადებს
num1 = 5
num2 = 10
print(num1 + num2)

# - აკლებს integer ტიპის ცვლადებს
num3 = 15
num4 = 8
print(num3 - num4)

# * მრავლდება integer ტიპის ცვლადებს
num6 = 7
num7 = 3
print(num6 * num7)

# / იყოფა integer ტიპის ცვლადებს მაფრამ ვიღებ float ტიპის შედეგს
num8 = 20  
num9 = 4
print(num8 / num9)

# % იღებს დარჩენილ ნაწილს integer ტიპის ცვლადების გაყოფის შემდეგ
num10 = 17
num11 = 5  
print(num10 % num11)
# ** ამატებს integer ტიპის ცვლადებს თავიანთ თავს რამდენჯერმე
num12 =2
num13 = 3
print(num12 ** num13)
# // იყოფა integer ტიპის ცვლადებს და იღებს მხოლოდ მთელ ნაწილს
num14 = 20
num15 = 3
print(num14 // num15)

#კონკატენაცია არის სტრინგების გაერთიანება.
str1 = "Hello"
str2 = "World"
print(str1 + " " + str2)
str3 = "Python"
str4 = "Programming"
print(str3 + " " + str4)

num1 =4
num2 = 6
print(num1 + num2)

name = "Mariam"
age=15
height = 1.51
print(f"Hello {name}, my age is {age} and my height is {height}")