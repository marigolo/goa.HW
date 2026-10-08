languages = {'html', 'css','JavaScript', 'python'}
languages.remove('JavaScript')
languages.add('React')
print(languages)



# 2)
city = {'USA', 'UK', 'Georgia', 'Brazil'}
city.clear()
city.add('Tbilisi')
city.add('London')
city.add('Brazil')
print(city)

# 3) რას გამოიტანს ეს კოდი? შედეგი ახსენით დეტალურად.

set1 = {'apple', 'banana', 'cherry'}
set2 = {'banana', 'orange'}
combo = set1.union(set2)
print(combo)
# დაპრინტავს {'orange', 'cherry', 'apple', 'banana'} 
# რადგან .union()- ფუნქცია აერთებს ორივე set-ს თუმცა ის არ გამოიტანს 2 banana 
# რადგან set-ში თავად ფილტრავს დუბლიკათელემენტებს