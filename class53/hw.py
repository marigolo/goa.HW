# 2)

def say_hello(func):
    def wrapper():
        print("ფუნქცია იწყებს მუშაობას...")
        func()
        print("ფუნქციამ დაასრულა მუშაობა!")
    return wrapper


@say_hello
def Hello():
    print("Hello!")


Hello()


# 3)

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        
        result = func(*args, **kwargs)

        end = time.time()

        print("დრო:", end - start, "წამი")

        return result
    return wrapper


@timer
def test():
    time.sleep(2)
    return "დასრულდა"


print(test())

# 11)

def decorator(func):
    def wrapper():
        print("Starting...")
        result = func()
        print("Finished!")
        return result
    return wrapper


@decorator
def hello():
    print("Hello!")


print(hello())


# 12)

def welcome(func):
    def wrapper():
        print("Welcome!")
        result = func()
        return result
    return wrapper


@welcome
def hello_person():
    print("Hello, i am Mari! who are you?")


hello_person()


# 13)

def line(func):
    def wrapper():
        print("--------------------")
        result = func()
        print("--------------------")
        return result
    return wrapper


@line
def greetings():
    print("Hello i am mari!")


greetings()