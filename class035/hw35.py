# 2)
# ა) set-ში ყველა ელემენტი უნიკალურია
# ბ) set-ში ელემენტებს არ აქვთ index-ები ანყ დაულაგებელია
# გ) set-ი არის mutable


# 3)
# ა) .clear()
# ბ) .add()
# გ) .union()
# დ) .different()
# ე) .set()

# ა)
name = {'Anna', 'Mj', 'Anamaria'}
name.clear()
print(name)

# ბ)
names = {'Anna', 'Mj', 'Anamaria', 'Kira'}
names.add('Lizi')
print(names)

# გ)
even = {2, 4, 6, 8}
odd = {1, 3, 5, 7, 9}
num = even.union(odd)
print(num)

# დ)
x = {3.9, 4,5, 1, 5}
y = {3, 9, 4, 5, 1, 5}
z = x.difference(y)
print(z)

# ე)
mylist = [3, 4, 5, 4 , 6, 6 ,4, 3, 3]
mylist = set(mylist)
mylist = list(mylist)
print(mylist)


# 4)
number = {3, 1, 2, 4, 6, 3, 5, 9, 0, 3}
print(number)

# 5)
Array = [1, 2, 2, 3, 4, 4, 5]
Array = set(Array)
Array = list(Array)
print(Array)

# 6)
fav  = {'Good girls guide to murder', 'Harry potter', 'The 100', 'Gifted'}
nam1 = len(fav)
print(nam1)

# 7)
week = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'}
for day in week:
    print("დღე:", day)
    
# 8)
football_players = {'დათო', 'ნიკა', 'ლუკა', 'ლიკა'}
basketball_players = {'ანი', 'ლუკა', 'მარიამი', 'ნიკა'}
players = football_players.union(basketball_players)
print('number of uninic people:', len(players))

# 9)
wishlist = {'Python', 'JavaScript', 'java', 'c++'}
learned = {'Python', 'HTML', 'CSS'}
to_learn = wishlist.difference(learned)
print(to_learn)

# 10)
cart = {101, 204, 305}
cart.clear()
print(cart)