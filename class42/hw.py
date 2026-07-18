'''
2)

პროგრამირებაში არის შეცდომების ორი  ძირითადი კატეგორია 
1. Bugs - იგი არის მცირე შეცდომა და კოდს არ აჩერებს
2. Exception  - იგი არის მაშტაბური შცდომაა და კოდის გაშვებას აჩერებს
    განვიხილეთ:
        ZeroDivisionError
        KeyError
        ValueError
        TypeError
        IndexError
        NameError


3)

ZeroDivisionError-ი წარმოიქმნება მაშინ,
როდესაც ვცდილობთ ნებისმიერი რიცხვი გავყოთ 0-ზე.
    მაგ:
        print(10 / 0)
        print(6 / 0)



6) 

finally - სრულდება ყოველთვის, 
მიუხედავად იმისა მოხდა try ბლოკში შეცდომა არის თუ არა

else - სრულდება მხოლოდ მაშინ, 
თუ try ბლოკში შეცდომა არ მოხდა

raise - გამოიყენება try ბლოკში ადამიანის 
შეცდომაზე გასფრთხილებლად

'''

# 4)

try:
    x = int(input('enter number x: '))
    y = int(input('enter number y: '))
    print(x / y)
except  ZeroDivisionError:
    print('you cant divide a number by 0')
    
    
# 5) 

me = {
    'name':'Mari',
    'age':15,
    'hight':'1.54'
}

try:
    print(me['email'])
except KeyError:
    print('Key does not exist')


# 7)

def divide(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        return 'Cant divide by zero.'


print(divide(20, 5))
print(divide(20, 0))

# 8)

try:
    print('Trying...')

except:
    print('Error encountered')

finally:
    print('Code cleanup is done')
    
    
# 9)

def check_pass(password):
    try:
        if len(password) < 8:
            raise ValueError('Password too short')

        if " " in password:
            raise ValueError('Password cannot contain spaces')

        return 'Password accepted'

    except ValueError as error:
        return error


print(check_pass('abc'))
print(check_pass('abc defgh'))
print(check_pass('mypassword123'))