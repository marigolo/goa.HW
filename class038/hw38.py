'''
1) Dictionary - არის მონაცემის ტიპი რომელიც 
შედგება kye -სა და value - საგან

'''

# 2) 

football = {
    'name' : 'Cristiano Ronaldo',
    'country' : 'Portugal',
    'goals_count' : '144 goals',
}

print(football)

# 3) 

menu = {
    'foods': ['ხინკალი', 'მწვადი', 'ქაბაბი']
}

print(menu["foods"][1])

# 4)

movie = {
    'title': 'Titanic',
    'year': 1997
}

movie['year'] = 1970

print(movie)

# 5)

student = {
    'name' : 'Mariam',
    'age' : 18
}

student.pop("age")

print(student)