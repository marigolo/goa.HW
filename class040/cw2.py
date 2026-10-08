# 1)

info = {
    'name' : 'Mari',
    'lastname' : 'Goloshvili',
    'age' : 15
}

print(info.items())


# 2)

numbers = [1, 2, 3, 4, 5]
dable = [x**2 for x in numbers ]
print(dable)


# 3)

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
odd = [x for x in number if x % 2 != 0]
print(odd)