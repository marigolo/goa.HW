# 2)

'''
filter (ფუნქცია, კოლექცია(list)) =  აბრუნებს ელემენტს რომელიც  შეასრულებს რაღაც კონკრეტულ მდგომარეობას
map(ფუნქცია, კოლექცია(list)) = ყველა ელემენტზე ასრულებს ფუნქციას ყველა ელემენტზე
'''

names = ["gio", "ana", "nika"]
capitalized = list(map(str.capitalize, names))
print(capitalized)

numbers = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)

# 3)

celsius = [0, 25, 100, -10, 37]
Kelvin = list(map(lambda x: x + 273, celsius))
print(Kelvin)

# 4)

num = [2, 7 ,-1, -8, -2, 9 , 0, 6]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)


# 5)

usernames = []

for i in range(5):
    name = input('Enter a name: ')
    usernames.append(name)

greet_users = list(map(lambda name: 'Welcome ' + name, usernames))

print(greet_users)

# 6)

cars = {
    'BMW': 1998,
    'Mercedes': 2005,
    'Toyota': 1995,
    'Audi': 2010,
    'Honda': 1999
}

old_years = list(filter(lambda car: car[1] < 2000, cars.items()))

print(old_years)

# 7)

usernames = []

for i in range(5):
    name = input('Enter a name: ')
    usernames.append(name)

filtered_users = list(filter(lambda name: len(name) > 5, usernames))

print(filtered_users)