day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case _:
        print("Weekend or invalid day")
        
        
        
'''
1) დაწერეთ მოცემული პროგრამა match case-ით. მოცემული გაქვთ ცვლადი month, რომელშიც შეინახავთ რომელიმე თვეს. თქვენი დავალებაა შეამოწმოთ month ცვლადი და მის მიხედვით დააბრუნოთ რომელი სეზონია (spring, summer, fall, winter). გამოიყენეთ დღეს ნასწავლი მასალა.

'''

month = 'April'

match month:
    case 'December' | 'January' | 'February':
        print('winter')
    case 'March' | 'April' | 'May':
        print('spring')
    case 'June' | 'July' | 'August':
        print('summer')
    case 'September' | 'October' | 'November':
        print('fall')