'''
1) შექმენი დეკორატორი, რომელიც ფუნქციის პასუხს თავში დ აბოლოში დაუმატებს '***'-ს.
2) შექმენი ფუნქცია, რომელიც ერთ ინტეჯერს აბრუნებს. შექმენი დეკორატორი, რომელიც ფუნქციის პასუხს 5-ს დაუმატებს. შექმენი სამი სხვა ფუნქცია, რომელიც სხვადასხვა ონტეჯერს დააბრუნებს და სამივეს იგივე დეკორატორი გაუწერე.
'''
# 1)

def stars(func):
    def wrapper():
        return "***" + func() + "***"
    return wrapper

@stars
def hello():
    return "Hello"


print(hello())

# 2) 

def add_five(func):
    def wrapper():
        return func() + 5
    return wrapper

@add_five
def one(): return 10

@add_five
def two(): return 20

@add_five
def three(): return 30

print(one())
print(two())
print(three())