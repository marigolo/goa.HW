# 2) შექმენით ფუნქცია, რომელიც პარამეტრად იღებს რიცხვების სიას და აბრუნებს ამ რიცხვების საშუალო მნიშვნელობას.
def average(num):
    return sum(num) / len(num)
nums = [40, 90, 30, 70]
print(average(nums)) 


# 3) შექმენით ფუნქცია, რომელიც პარამეტრად იღებს რიცხვების სიას და აბრუნებს ამ სიაში ლუწი რიცხვების რაოდენობას.
def count_even(number):
    count = 0
    for num in number:
        if num % 2 == 0:
            count += 1
    return count
number = [4, 7, 9, 6, 8]
print(count_even(number))

  
# 4) შექმენით ფუნქცია, რომელიც პარამეტრად იღებს რიცხვების სიას და აბრუნებს ამ სიაში კენტი რიცხვების რაოდენობას.
def count_odd(numbers):
    count = 0
    for num1 in numbers:
        if num1 % 2 != 0:
            count += 1
    return count
numbers = [4, 7, 9, 6, 8]
print(count_odd(numbers))


# 5)  შექმენით ფუნქცია სახელწოდებით double_values რომელიც არგუმენტად მიიღებს სიას და დააბრუნებს ახალ სიას, სადაც თითოეული ელემენტი გაორმაგებული იქნება.
def double(numbers):
    results = []
    for num2 in numbers:
        results.append(num2 * 2)
    return results
num_list = [9, 2, 3, 8, 6]
print(double(num_list))


# 6) შექმენით ფუნქცია და გადაეცით არგუმენტად სია. ფუნქციამ უნდა დააბრუნოს ახალი სია, რომლის თითოეული ელემენტიც უნდა იყოს კვადრატში აყვანილი.
def square(lists):
    new_list = []
    for num3 in lists:
        new_list.append(num3 ** 2)
    return new_list
list_mine = [1, 6, 5, 10, 20]
print(square(list_mine))
    
    
# 7) შექმენით ფუნქცია სახელწოდებით sum, რომელსაც არგუმენტად გადაეცემა 3 რიცხვი და ფუნქციის მიზანი იქნება, რომ ამ სამი რიცხვის ჯამი დააბრუნოს.
def sum(number1, number2, number3):
    return number1 + number2 + number3
print(sum(2, 4, 6))

# 8) შექმენით ფუნქცია სახელწოდებით substract, რომელსაც არგუმენტად ორ რიცხვს. ფუნქციამ პასუხად უნდა დააბრუნოს ამ რიცხვების სხვაობა.
def substract(number4, number5):
    return number4 - number5
print(substract(6, 2))


# 9)  შექმენით ფუნქცია სახელწოდებით multiply, რომელსაც არგუმენტად ორ რიცხვს. ფუნქციამ პასუხად უნდა დააბრუნოს ამ რიცხვების ნამრავლი.
def multiply(number6, number7):
    return number6 * number7
print(multiply(7, 8))


# 10)  შექმენით ფუნქცია check_age, რომელიც არგუმენტად მიიღებს მომხმარებლის ასაკს.
# თუ მომხმარებლის ასაკი მეტი ან ტოლი იქნება 18-ზე, ტერმინალში დაიბეჭდოს "Access Granted", წინააღმდეგ შემთხვევაში – "Access Denied".
def check_age(age):
    if age == 18:
        return 'Access Granted'
    else:
        return 'Access Denied'
print(check_age(int(input('Enter your age '))))


# 11) შექმენით ფუნქცია print_names, რომელიც მიიღებს სახელების სიას და ტერმინალში თითოეული მათგანს ცალ-ცალკე ხაზზე დაბეჭდავს.
def print_names(names):
    for name in names:
        print(names)
name_list = ['Mari', 'Lika', 'Anamaria', 'Ana']
print(name_list)

# 12) დაწერეთ ფუნქცია სახელწოდებით odd_or_even. ფუნქციამ უნდა დააბრუნოს Even თუ არგუმენტად გადაცემული რიცხვი ლუწია, ხოლოდ Odd - თუ კენტი.
def odd_or_even(number):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'odd'
print(odd_or_even(4))


# 13) შექმენით ფუნქცია student_grade, რომელიც იღებს მოსწავლის ქულას (0-დან 100-მდე) და ტერმინალში დაბეჭდავს შემდეგ ქულებს:
#     • 90-100: - A
#     • 70-89: - B
#     • 50-69: - C
#     • 0-49: - F
def student_grade(grade):
    if 90 <= grade <= 100:
        return 'A'
    elif 70 <= grade <= 89:
        return 'B'
    elif 50 <= grade <= 69:
        return 'C'
    elif 0 <= grade <= 49:
        return 'F'
grade_input = int(input('Enter your grade: '))
print(student_grade(grade_input))


# 14) დაწერეთ ფუნქცია, რომელიც არგუმენტად მიიღებს მომხმარებლის სახელს, გვარს და ასაკს. ფუნქციამ უნდა დააბრუნოს მომხმარებლის მონაცემები წინადადების სახით. (გამოიყენეთ f string-ი)
def user_info(first_name, last_name, age):
    return f'your name is {first_name} {last_name} and your age is {age}.'
name = input('enter your name ')
surname = input('enter your surname ')
age = int(input('anter your age '))
print(user_info(name, surname, age))


#15) შექმენით ფუნქცია - Arithmetic_mean, რომელიც პარამეტრად მიიღებს სიას. ფუნქციამ სიაში არსებული ელემენტების საშუალო არითმეტიკული უნდა დააბრუნოს. (ფუნქცია გათვლილი უნდა იყოს ნებისმიერი რაოდენობის შემცველ სიაზე)
def Arithmetic_mean(lst):
    if len(lst) == 0:
        return 0
    total = 0
    for num in lst:
        total += num
    return total / len(lst)
print(Arithmetic_mean([1, 2, 3, 4, 5]))


# 16) შექმენით ფუნქცია და არგუმენტად გადაეცით String-ი. ფუნქციამ უნდა "გაფილტროს" ეს სტრინგი თანხმოვანი ასოებისგან და მხოლოდ დააბრუნოს ის ხმოვანი ასოები, რომლებსაც ეს სტრინგი შეიცავს.
def filter(s):
    vowels = "aeiou"
    result = ""
    for i in s.lower():
        if i in vowels:
            result += i
    return result
print(filter("Hello World"))


# 17)  შექმენით ფუნქცია, რომელიც პარამეტრად მიიღებს სიას და დააბრუნებს ახალ სიას, სადაც მხოლოდ უნიკალური ელემენტები იქნება — ანუ თქვენი დავალებაა სია გაფილტროთ duplicate ელემენტებისგან.
def unique(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
        else:
            pass
    return result
lists = [1, 1, 2, 2, 3, 4, 4, 5]
print(unique(lists))


# 18) შექმენით manual sum ფუნქცია Python-ში. (manual ნიშნავს გარკვეული ფუნქციის/მეთოდის საკუთარი ხელით შექმნას.)
# ეს ფუნქცია უნდა მუშაობდეს სიებზე, კონკრეტულად: მან უნდა დააბრუნოს სიის ყველა ელემენტის ჯამი.

def manual_sum(lst):
    total = 0
    for i in lst:
        total += i
    return total
new = [2, 5, 6, 0]
print(manual_sum(new))



