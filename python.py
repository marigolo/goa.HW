# # x = 1
# # y = 2

# # if x:
# #     if y:
# #         print('A')
# #     else:
# #         print('B')
# # else:
# #     print('C')
    
    
# # s = 'hello'
# # s = s.capitalize()

# # for i in range(5):
# #     if i == 2:
# #         pass
# #     print(i)

# # nums = [3, 5, 1, 6, 2, 4]
# # print(nums)
# # nums.sort()
# # print(nums)

# # nums = [3, 5, 1, 6, 2, 4]
# # result = sorted(nums)
# # print(nums)
# # print(result)







# # def sort_lists(a, b):
# #     a.sort()
# #     b.sort()
# #     return  a + b


# # print(sort_lists([2,5,6,7,8], ['c', 'b', 'a']))  










# # nums = [3, 5, 1, 6, 2, 4]
# # nums1 = ['b', 'c', 'a']
# # nums.sort()
# # nums1.sort()

# # together = nums + nums1
# # print(together)



# # nums = [3, 5, 1, 6, 2, 4]
# # nums1 = ['b', 'c', 'a']

# # for i in nums:
# #     nums = sorted(nums)
# # for i in nums1:
# #     nums1 = sorted(nums1) 
# # together = nums + nums1
# # print(together)


# # def add(*args):
# #     return sum(args) 
    

# # print(add(10, 12, 13, 15))

# # def multify(**kwargs):
# #     for key, value in kwargs.items():
# #         return  key + ':' + value
    
# # print(multify(
# #     name = 'mari', age = 15
# # ))


# # word = 'Hello  World I am learning'
# # spleted = word.split()
# # added = '-'.join(word)
# # print(added)
# # print(spleted)


# # class Car:
# #     def __init__(self, color, brend, year):
# #         self.__color = color
# #         self.brend = brend
# #         self.year = year
        
# #     def color_display(self):
# #         return f'color of this car is {self.__color}'
        
# # car1 = Car('red', 'BMW', '2026')
# # car2 = Car('Black', 'Toyota', '2023')

# # # print(car1.__color)
# # print(car1.color_display())



# # class User:
# #     def __init__(self, name, age, birth):
# #         self.name = name
# #         self.age = age
# #         self.birth = birth
        

# # usr1 = User('Mari', 15, 2011)
# # print(usr1.name)
# # print(usr1.age)
# # print(usr1.birth)

# # class Animal:
# #     def __init__(self, name, breed, color):
# #         self.name = name
# #         self.breed = breed
# #         self.color = color

# #     def make_sound(self):
# #         return "making sound"


# # class Cat(Animal):
# #     def __init__(self, name, breed, color):
# #         super().__init__(name, breed, color)

# #     def make_sound(self):
# #         return "mew" # ეწოდება Polymorphism


# # cat1 = Cat("miki", "british", "white")

# # print(cat1.make_sound())


# class Father:
#     def __init__(self, drives):
#         self.drives = drives 
        
# class Mother:
#     def __init__(self, cook):
#         self.cook = cook


# class Child(Mother, Father):
#     def __init__(self, cook, drives):
#         Mother.__init__(self, cook)
#         Father.__init__(self, drives)
        

# child1 = Child('yess', 'yes')

# print(child1.cook)
# print(child1.drives)
        


n = 5

# for i in range(1, n +1):
#     pass
#     # print(' ' * (n - i) + '*' *(2 * i - 1))
    
# for i in range(n - 1, 0, -1):
#     print(' ' * (n - i) + '*' *(2 * i - 1))


# def show(**kwargs):
#     print(kwargs)
    
# show(
#     name = 'Masha',
#     age = 12, 
#     tear = True
# )



x = int(input('Enter your age: '))

if x % 2 == 0:
    print(x)
else:
    print(x + 1)