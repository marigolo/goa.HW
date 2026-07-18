# 1)
num1 = int(input('rnter a number x: '))
num2 = int(input('rnter a number y: '))

try:
    devaid = num1 / num2
    print(devaid)
except ValueError:
    print('ValueError')
except ZeroDivisionError:
    print('ZeroDivisionError you cannt divide on 0')
    
# 2)

num3 = int(input('enter a number: '))

try:
    print('You entered:', num3)

except ValueError:
    print('Please Enter numbers only.')
    