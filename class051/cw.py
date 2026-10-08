# 1)

def show_info(name, *args):
    print('Name:', name)
    print('Type:', type(args))

    print('Args values:')
    for i in args:
        print(i)


show_info('Mari', 10, "Hello", True, 25.5)

# 2)

def find_sum(*sum):
    total = 0

    for num in sum:
        if num % 2 == 0:
            total += num

    print('Sum is:', total)


find_sum(5, 10, 7, 8, 17, 12, 3, 20, 45)


# 3)

def show_names(**name):
    print('Type:', type(name))
    print('Dictionary:', name)

    print("Values:")
    for value in name.values():
        print(value)


show_names(
    person1 = 'Mari',
    person2 ='Nino',
    person3 = 'Giorgi',
    person4 = 'Luka'
)


# 4)

def data(name, *args, **kwargs):
    print('Regular argument:', name)
    print('Args:', args)
    print('Kwargs:', kwargs)


data('Mari', 10, 20, 30, city = 'Tbilisi' , age = 15)