#or
num24 = True or False
print(num24)
#True

num25 = False or True 
print(num25)
#True

num26 = True or True
print(num26)
#True

num27 = False or False
print(num27)
#False

#and
num28 = True and False
print(num28)
#False

num29 = False and True 
print(num29)
#False

num30 = True and True
print(num30)
#True

num31 = False and False
print(num31)
#False


num_1 = True and False or False or True and True and False or True

# გამოიტანს True რადგან True and False= False , True and True= True , True and False = False , False or True = True , False or True = True , False or True = True

nam=int(input("what is the number of family mambers "))
thief_detected = nam > 4
print(thief_detected)