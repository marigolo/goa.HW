# 2)

def check_status1(code):
    if code == 200:
        return 'OK'
    elif code == 201:
        return 'Created'
    elif code == 400:
        return 'Bad Request'
    elif code == 404:
        return 'Not Found'
    elif code == 500:
        return 'Internal Server Error'
    else:
        return 'Unknown Status'
    
print(check_status1(200))

#  using match and  case
def check_status2(code):
    match code:
        case 200:
            return 'OK'
        case 201:
            return 'Created'
        case 400:
            return 'Bad Request'
        case 404:
            return 'Not Found'
        case 500:
            return 'Internal Server Error'
        case _:
            return 'Unknown Status'


print(check_status2(200))


# 3)

def analyze_point1(point):
    x, y = point
    if x == 0 and y == 0:
        return 'საწყისი წერტილი'
    elif x == 0:
        return 'მდებარეობს Y ღერძზე'
    elif y == 0:
        return 'მდებარეობს X ღერძზე'
    else:
        return f'წერტილი ({x}, {y}) სიბრტყეზეა'
    
print(analyze_point1((0, 0)))

# using match and  case

def analyze_point2(point):
    x, y = point
    match (x, y):
        case (0, 0):
            return 'საწყისი წერტილი'
        case (0, _):
            return 'მდებარეობს Y ღერძზე'
        case (_, 0):
            return 'მდებარეობს X ღერძზე'
        case _:
            return f'წერტილი ({x}, {y}) სიბრტყეზეა'


print(analyze_point2((0, 0)))
    
    
# 5)

def analyze_list1(lst):
    if len(lst) == 0:
        return 'სია ცარიელია'
    elif len(lst) == 1:
        return f'სია შეიცავს 1 ელემენტს: {lst[0]}'
    elif len(lst) == 2:
        return f'სია შეიცავს 2 ელემენტს: {lst[0]} და {lst[1]}'
    else:
        return f'შეიცავს მინიმუმ 2 ელემენტს, დანარჩენი: {lst[2:]}'

print(analyze_list1([5]))

#  using match and  case

def analyze_list2(lst):
    match len(lst):
        case 0:
            return 'სია ცარიელია'
        case 1:
            return f'სია შეიცავს 1 ელემენტს: {lst[0]}'
        case 2:
            return f'სია შეიცავს 2 ელემენტს: {lst[0]} და {lst[1]}'
        case _:
            return f'შეიცავს მინიმუმ 2 ელემენტს, დანარჩენი: {lst[2:]}'


print(analyze_list1([5]))
    
# 6)

def calculator1(command):
    operation, a, b = command

    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b == 0:
            return 'ნულზე გაყოფა არ შეიძლება'
        return a / b
    else:
        return 'უცნობი ოპერაცია'
    
print(calculator1(('+', 5, 3)))

#  using match and  case

def calculator2(command):
    operation, a, b = command

    match operation:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            if b == 0:
                return 'ნულზე გაყოფა არ შეიძლება'
            return a / b
        case _:
            return 'უცნობი ოპერაცია'


print(calculator2(('+', 5, 3)))