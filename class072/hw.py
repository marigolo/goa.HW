
# 2) Tuple unpacking ეწოდება, როდესაც Tuple-ის ელემენტებს ცალკეულ ცვლადებს ვანიჭებთ.

#  მაგალითი 1:
colors = ('Pink', 'Blue', 'Purple')
a, b, c = colors
print(a)
print(b)
print(c)

#  მაგალითი 2:
items = ('Book', 'Pan', 'Notbook')
d, e, f = items
print(d)
print(e)
print(f)

#  მაგალითი 3:
items = ('Book', 'Pan', 'Notbook')
d, e, f = items
print(d)
print(e)
print(f)

# მაგალითი 4:
lenguage = ('English', 'Georgian', 'Russian', 'Turkish')
g, h, *i = lenguage
print(g)
print(h)
print(i)

# 3) 

info = ('Mariam', 15, 'purple', 'Tbilisi', 'Student')
name, age, fav_color, city, statuse = info
print(name)
print(age)
print(fav_color)
print(city)
print(statuse)

# 4) 

numbers = (1, 2, 3, 4, 5, 6)
num1, *rest = numbers
print(num1)
print(rest)

# 5) set-ი არ ინახავს დუბლიკატებს, მას არ აქვს ინდეხსები

 
# 6)

nums = {1, 2, 2, 1, 3, 4, 3, 6, 7, 7}
print(nums)

# 7)

num_arrey = [1, 2, 2, 3, 4, 4, 5]
print(list(set(num_arrey)))


# 8)

books = {'Good girls guid to murder', 'As good as dead', 'Good girl bad blood', 'Six of crows', 'Inheritanse games'}
print(len(books))

# 9)

week_days = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'}

for day in week_days:
    print('დღეს: ' + day)
    
# 10) 

football_players = {'დათო', 'ნიკა', 'ლუკა', 'ლიკა'}
basketball_players = {'ანი', 'ლუკა', 'მარიამი', 'ნიკა'}
print(len(football_players.union(basketball_players)))

# 11)

wishlist = {'Python', 'JavaScript', 'HTML', 'CSS', 'React'}
learned = {'Python', 'HTML', 'CSS'}
print(wishlist.difference(learned))

# 12) 

cart = {101, 204, 305}
cart.clear()
print(cart)

# 13)

footballer = {
    'name': 'Cristiano Ronaldo',
    'country': 'Portugal',
    'goals_count': 950
}
print(footballer['name'])
print(footballer['country'])
print(footballer['goals_count'])

# 14)

students = {
    'Nika': 85,
    'Ana': 45,
    'Luka': 60,
    'Mariam': 40
}
students['Giorgi'] = 90
students['Ana'] = 75
passed_students = [name for name, grade in students.items() if grade > 50]
print(passed_students)

# 15)
num = [1, 2, 3, 4, 5, 6]
squares = [num ** 2 for num in numbers]
even_squares = [num for num in squares if num % 2 == 0]
print(squares)
print(even_squares)

# 16)

words = ['Python', 'AI', 'Development', 'Code', 'Learning', 'Data']
new_words = [word for word in words if len(word) > 4]
print(new_words)

# 17)

products = {
    'Apple': 2,
    'Milk': 4,
    'Bread': 3,
    'Chocolate': 5,
    'Juice': 4
}
expensive_products = [name for name, price in products.items() if price > 3]
print(expensive_products)