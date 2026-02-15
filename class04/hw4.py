#მაგალიტად: 2) 1.როცა ცვლადს ვარქმევთ არალოგიკურ სახელებს 
#2.როცა ცვლადს ვარქმევთ ისეთ სახელებს რომელიც მასშ შენახულ ინფორმაციას არ შეესბამება
#3.როცა ცვლადებს ვარქმევთ ერთიდაიგივე სახელებს
#3)კოდის გასწორებას ეწოდება Debugging რადგან 1940წ-ს კომპიუტერში კოდი ვეღარ გაეშვა კომპიუტერის შემოწმების შედეგად იპოვეს ხოჭო  ამიტომ შეცდომას დაარქვეს bug და მის მოშორება/გასუფთავებას debugging
#4)1.syntax errors არის კოდის წესების დარღვევიტ გამოწვეული ერორი რომელიც ხელს უშლის კოდის გაშვებას
#2.indentation errors,ხდება როცა ვიყენებთ ზედმეტ გამოტოვებას
#3.name errors, როცა ვიყენებთისეთო ცვლადის სახელს რომელიც ჯერ არ შეგვიქმნია
#4.type errors, როცა სტრინგ ტიპის ელემენტს და ინტეჯერ ელემენტს შორის ვახდენთ მათემატიკურ ოპერაციებს

#1)პრინტში მყოფი ცვლადი არ არსებობდა
name = "lika"
print(name)

#2) არ შეიზლება ინტეჯერ ელემენტსა  და  სტრინგ ელემენტს შორის არ შეიძლება მათემატიკური ოპერაციების ჩატარება
number = "5"
text = " apples"
result = number + text
print(result)

#3)სტრინგ ტიპის ელემენტს აუცილებელი ქონდეს კლანჭები ასევე ცვლადის სახელი ხუსტად უნდა გადავიტანოთ
name = "liKa"
name2 = name + "4"


# 4) არ შეიძლება ცვლადის სახელი იწყებოდეს ციფრით
first_user = "Lika"
nduser2 = "Giorgi"
print(first_user)

#5)არ შეიძლება ცვლადის სახელში გამოტოვების გამოყენება
first_name = "Data"
last_name = "random"

#6)არ შეიძლება ცვლადის სახელი იწყებოდეს ციფრით
first_user = "Lika"
nduser3 = "Giorgi"
print(first_user)

#7)
city= input("enter your city")
Distric = input("enter your District")
building = input("enter your building number")
print(f"your city is {city} your distsrict is {Distric} and your building number is {building}")

#8)
age = input("enter your age")
print(f"you are {age} years old")

num1 = input("enter your lucky number")
num2 = input("enter your last favorite number")
print(num1 + num2)