def string_to_integer(s):
    if not s.isdigit():
        return "invalid Input"
    elif '-' in s:
        return int(-s)
    else:  
        return int(s)

print(string_to_integer("-123"))
    
    
    
# შექმენით ფუნქცია, რომელიც string რიცხვს გადაიყვანს ინტეჯერად. გაითვალისწინეთ: დაამატეთ შემოწმება არგუმენტი შეიცავს თუ არა დამატებით სიმბოლოებს (ასოები, !@#$%^&*()+).
# თუ აღმოჩნდება, რომ შეიცავს => გამოიტანეთ "invalid Input".