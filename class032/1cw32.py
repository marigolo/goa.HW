my__tuple = ('red', 'blue', 'green')
# unpacking
cherry,apple,banana = my__tuple
print(cherry)
#თუ ელემენტების რაოდენობა არ ემთხვევა unpackingს ელემენტებს მაშინ გამოვა error
#asteriqs =* დანარჩენი ელემენტები რაზეც გამოვიყენებთ გამოდის სიით 




# 1) შექმენი Tuple,  რომელიც შეიცავს 5 შენს საყვარელ ფილმს. დაბეჭდე  Tuple-ის 
# ყველა ელემენტი ცალცალკე ამ ელემენტის მონაცემის ტიპთან ერთად. (მაგ. 'Interstellar', <class 'str'>)
tuple1 = ('X-Men', 'The 100', 'Avatar', 'Joker', 'Gifted')

for movie in tuple1:
    print(movie, type(movie))


#2) ჩამოწერეთ რა მსგავსება და განსხვავებაა List-ებსა და Tuple-ბს შორის.

    #List-ის შეცვლა შეიძლება 
    #Tuple-ის შეცვლა არ შეიძლება
#3) ახსენით რას აკეთებს Asterisk ოპერატორი და მოიყვანეთ მინიმუმ 2 მაგალითი.
#დანარჩენი ელემენტებს ნომრავს და ინახავს ცვლადში  გამოაქვს სია
my__tuple2 = (1,2,3,4,5)
num1,num2,*rest_num = my__tuple2  
my__tuple3 = (1,2,3,4,5,6)
num1,num2,*rest_num = my__tuple3  

#4) შექმენით Tuple, სადაც შეინახავთ 7 ელემენტს. გამოიყენეთ Tuple Unpacking იმისთვის, რომ 4 სხვადასხვა 
# ცვლადში გადაანაწილოთ Tuple-ის ელემენტები. ოთხივე ცვლადი დაბეჭდეთ ტერმინალში.
tulips4 = (1,3,4,6,8,9,8)
a,b,c,d,*rest = tulips4
print(a)
print(b)
print(c)
print(d)
print(rest)