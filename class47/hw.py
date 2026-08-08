# 2)

info = lambda name , surname , age : f'name: {name}, surname: {surname} , age: {age}'
print(info('Mariam', 'Goloshvili', 15))

# 3)

average = lambda num : sum(num) / len(num)
print(average([10, 20, 30, 40]))

# 4)

palindrome = lambda text : text == text[::-1]
print(palindrome('level')) 
print(palindrome('hello'))  

# 5)

check_number = lambda num : 'Positive' if num > 0 else 'Negative' if num < 0 else 'Zero'
print(check_number(12))
print(check_number(-8))
print(check_number(0))

# 6)

multiply_by_two = lambda numbers : [x * 2 for x in numbers]
print(multiply_by_two([1, 2, 3, 4]))

# 7)

long_strings = lambda strings : [s for s in strings if (lambda x : len(x) > 5)(s)]
print(long_strings(["apple", "banana", "kiwi", "strawberry"]))

# 8)

negative_numbers = lambda number: [n for n in number if (lambda x: x < 0)(n)]
print(negative_numbers([5, -3, 7, -1, 0, -8]))