def string_to_integer(s):
    if not s.isdigit():
        return "invalid Input"
    elif '-'  in s:
        return int(s)
    else:  
        return int(s)

print(string_to_integer("-123"))
    
    
    
    
# def string_to_integer(s):
#     if not s.isdigit():
#         return "invalid Input"
#     return int(s)
# # ტესტირება
# print(string_to_integer("-123"))  # Output: 123
# print(string_to_integer("123a"))  # Output: invalid Input
    


def string_to_int(s):
    if len(s) == 0:
        return "invalid Input"
    start = 0
    is_negative = False

    if s[0] == '-':
        is_negative = True
        start = 1

    if start == len(s):
        return "invalid Input"

    result = 0

    for i in range(start, len(s)):
        ch = s[i]

        if ch < '0' or ch > '9':
            return "invalid Input"

        result = result * 10 + (ord(ch) - ord('0'))

    if is_negative:
        result = -result

    return result



print(string_to_int("123"))      # 123
print(string_to_int("-456"))     # -456
print(string_to_int("12a3"))     # invalid Input
print(string_to_int("12!3"))     # invalid Input
print(string_to_int("--12"))     # invalid Input
print(string_to_int("ss"))        # invalid Input