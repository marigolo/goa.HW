# 1)

import time

seconds = int(input("რამდენი წამი? "))

while seconds > 0:
    print(seconds)
    time.sleep(1)
    seconds -= 1

print("დრო ამოიწურა!")

# 1.2

import time

def call_decorator(func):
    def wrapper():
        print(" ზარი იგზავნება...")
        time.sleep(2)
        func()
        print(" ზარი დასრულდა")

    return wrapper


@call_decorator
def call():
    print("ზარი მიღებულია!")


call()