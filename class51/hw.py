# 1)
def sum_number(*args):
    return sum(args)
print(sum_number(2, 7, 0))

# 2)

def largest_number(*args):
    return max(args)
print(largest_number(1, 4, 5, 7))

# 3)

def count_even1(*args):
    totle = 0
    for x in args:
        if x % 2 == 0:
            totle += 1
    return totle
print(count_even1(2, 7, 10, 15, 18))

def count_even2(*args):
    return sum(1 for i in args if i % 2 == 0)
print(count_even2(2, 7, 10, 15, 18))

# 4)

def average(*args):
    return sum(args) / len(args)
print(average(10, 20, 30))

# 5)

def info(name, age, *args):
    return f'My name is : {name}, My age is : {age} and info about me is: {args}'
print(info('mari', 15, 'Georgia', 'learning python'))

# 6)
        
def print_info(**kwargs):
    return kwargs.items()
print(list(print_info(name='Mari', age=15, city='Tbilisi')))

# 7)

def print_values1(**kwargs):
    return kwargs.values()
print(list(print_values1(name='Mari', age=15, city='Tbilisi')))

def print_values(**kwargs):
    for value in kwargs.values():
        print(value)

print_values(name='Mari', age=15, city='Tbilisi')


# 8)

def count_keys(**kwargs):
    return len(kwargs)
print(count_keys(name='Mari', age=15, city='Tbilisi'))

# 9)

def my_function(name, age, *args, **kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)


my_function("Mari", 15, "Python", "HTML", city="Tbilisi", hobby="coding")
# 'Mari' არის პირველი რეგულარული არგუმენტი ინახება name-ში.
# 15  არის მეორე რეგულარული არგუმენტი ინახება age-ში.
# 'Student', 'Georgia' არიან ზედმეტი positional არგუმენტები ინახება *args-ში (tuple).
# hobby='Coding', city='Tbilisi' არიან  keyword არგუმენტები ინახება **kwargs-ში (dictionary).

# 10)

def sum_numbers(**kwargs):
    total = 0
    for value in kwargs.values():
        if type(value) == int or type(value) == float:
            total += value
        return total
print(sum_numbers(a=10, b='hello', c=5, d=2.5, e='Python'))

# 11)

def decorator(func):
    def wrapper():
        print('Starting...')
        func()
        print('Finished!')
    return wrapper

@decorator
def hello():
    return 'Hello!'
print(hello())

# 12)

def welcome(func):
    def wrapper():
        print('Welcome!')
        func()
    return wrapper

@welcome
def hello_person():
    return 'Hello,i am Mari!'
print(hello_person())

# 13)

def line(func):
    def wrapper():
        print('--------------------')
        func()
        print('--------------------')
    return wrapper

@line
def greetings():
    return 'Hello!'
print(greetings())