'''
class Metod - გამოიძახება უშუალოდ კლასზე და არა ცალკეულ ინსტანციებზე. ეს საშუალებას გვაძლევს, გამოვიყენოთ ისინი კლასის ინსტანციის შექმნის გარეშე. ისინი განსაკუთრებით სასარგებლოა ისეთი მოქმედებებისთვის, რომლებიც მთლიანად კლასს ეხება და არა კონკრეტულ ობიექტს. 

ინსტანციები იზიარებენ ყველაფერს, რაც კლასს აქვს, მათ შორის class მეთოდებსაც. ეს ნიშნავს, რომ class მეთოდის გამოძახება ინსტანციებიდანაც შეგიძლიათ.

Static methods  - არ გადაეცემა cls ანუ მათ იკლასის მდგომარეობაზე წვდომა არ აქვთ მას ვიყენებთ როდესაც როცა არ ვიცით კლასსის სინტაკსი

'''

# class Metod  ex1:

class Book:
    
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # 1) regular method
    def describe_book(self):
        print(self.title, 'by', self.author)

    # 2) class method
    @classmethod
    def books_in_series(cls, series_name, number_of_books):
        print('There are', number_of_books, 'books in the', series_name, 'series')

    # 3) class method
    @classmethod
    def dysplayinfo(cls, title, author):
        print(title, 'by', author)


# Creating an instance of Book
my_book = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling")

# Using the instance method
my_book.describe_book()

# Calling the class method on the instance
my_book.books_in_series("Harry Potter", 7)

# Calling the class method
my_book.dysplayinfo("Harry Potter", "J.K. Rowling")


# ----------- cw ---------



# 1)

class Movie:
    def __init__(self, movieTitle, director, year):
        self.movieTitle = movieTitle
        self.director = director
        self.year = year
    
    @classmethod
    def display_info(cls, movieTitle, director, year):
        return f'Movi name: {movieTitle}, Movis director  is {director}, year of movie is {year}'


print(Movie.display_info('Harry Potter', 'jj', 1123))

# 2)

class Profile:
    def __init__(self, username, creationDate):
        self.username = username
        self.creationDate = creationDate
    
    @staticmethod
    def get_user_info(username, creationDate):
        return f'username is: {username} and creationDate is: {creationDate}'
    
print(Profile.get_user_info('Mari', '2025 - 10 - 12'))
    
