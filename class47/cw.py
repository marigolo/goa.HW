# def add(a ,b):
#     return a + b
# res1 = add(1 , 3)
# print(res1)

# def greed():
#     return 'Hello'

# def name(user):
#     return user


# def add(a ,b):
#     return a + b

# def high(use):
#     return f'return: {use}'
# print(high(add(5, 9)))

# --------------------lambda-------------------
# add = lambda x, y: y + x

# print(add(3,7))

# greet = lambda name : f'hello {name}'
# print(greet('mari'))

# hesh = lambda word: '#' + word
# print(hesh('lizi'))

# hash = lambda word: '#' + ''.join(word.split())
# print(hash('good morning'))

# def mult (n):
#     return lambda a: a * n
# dable = mult(2)
# print(dable(8))

# def add(n):
#     return lambda x: x + n
# lambda1 = add(5)
# print(add(4))
# -------------------------------------------------------------

'''
1) შექმენით lambda ფუნქცია double, რომელიც არგუმენტად მიიღებს რიცხვს და პასუხად დააბრუნებს გაორმაგებულს.

2) შექმენით lambda ფუნქცია check_odd, რომელიც შეამოწმებს რიცხვი კენტია თუ არა. თუ კენტია - აბრუნებს True-ს. სხვა შემთხვევაში False-ს.
'''

# 1)
double = lambda x : x * 2
print(double(2))

# 2)
check_odd = lambda y: y % 2 != 0
print(check_odd(6))
print(check_odd(9))