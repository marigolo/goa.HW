# def greet():
#     print('Hello')
    
# greet()

# def greed_user(name):
#     print(f'Hello {name}')
    
# greed_user(input('enter your name '))

# def multuply(x,y):
#     print(x+y)
    
# multuply(20,98)


# def devaid(a,b):
#     print(a//b)
    
# devaid(22,44)

# def prconal_greet(name):
#     print(f'hello{name}')
    
# prconal_greet('mari')

# def dable(num):
#     print(num * 2)
    
# print(22)

# def GREET():
#     return 'Hello'

# print(GREET())

# def even_or_odd(num):
#     if num % 2 == 0:
#         return 'even'
#     else:
#         return 'odd'
    
# print(even_or_odd(33))
# print(even_or_odd(14))
# print(even_or_odd(20))
# print(even_or_odd(11))

# def check_c(name):
#     if name == name.capitalized():
#         return 'your name starts with upercase letter'
#     else:
#         return 'your name is nor copitalazed'


def greed_user(name):
    return f'Hello{name}'
    
print(greed_user(input('enter your name ')))

def multuply(x,y):
    return x + y 
print(multuply(20,980))


def even_or_odd(num):
    if num % 2 == 0:
        return 'even'
    else:
        return 'odd'
print(even_or_odd(33))
print(even_or_odd(14))
print(even_or_odd(20))
print(even_or_odd(11))

def dable(num):
    return num ** 2
    
print(dable(22))

def word1(words):
    return len(words)
print(word1('Hello'))

def reverse(word):
    return word[::-1]
print(reverse('helo i am mari'))

def list(numbers):
    return sum(numbers)
print(list([1, 2, 3, 4]))  

def check_age(name, age):
    if age >= 18:
        return f"{name} is adult"
    else:
        return f"{name} is not adult"
    
print(check_age("Giorgi", 20))  
print(check_age("mari", 15))     