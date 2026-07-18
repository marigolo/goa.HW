# 6)

students = {
    "Ana": 85,
    "Gio": 45,
    "Nino": 72
}

students["Luka"] = 90
students["Gio"] = 60
passed_students = [name for name, grade in students.items() if grade > 50]

# 7)

numbers = [1, 2, 3, 4, 5, 6]
squares = [num ** 2 for num in numbers]
even_squares = [num for num in squares if num % 2 == 0]


# 8)

words = ["Python", "AI", "Development", "Code", "Learning", "Data"]
long_words = [word for word in words if len(word) > 4]
print(long_words)

# 9)

products = {
    "Apple": 5,
    "Bread": 2,
    "Milk": 1,
    "Water": 6,
    "Cheese": 7
}

expensive_products = [product for product, price in products.items() if price > 3]