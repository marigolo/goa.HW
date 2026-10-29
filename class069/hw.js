/* 
2) შექმენით მასივი, სადაც შეინახავთ რიცხვებს. თქვენი დავალებაა, რომ filter მეთოდის გამოყენებით ახალ მასივში ჩაამატოთ ის რიცხვები, რომლებიც ლუწია. კომენტარების სახით ახსენით ცვლის თუ არა filter მეთოდი ორიგინალ მასივს და აბრუნებს თუ არა ის მნიშვნელობას.

3) შექმენით მასივი სადაც შეინახავთ სახელებს. თქვენი დავალებაა, რომ map მეთოდის გამოყენებით გამოიტანოთ თითოეული სიტყვის პირველი ასო და გადააქციოთ ის დიდ ასოდ. callback ფუნქციის მიერ დაბრუნებული მნიშვნელობა შეინახეთ ახალ მასივში, map ფუნქციის მიერ დაბრუნებული ახალი მასივი კი გამოიტანეთ console - ში.

4) 5 მომხმარებელის სახელი შეინახეთ usernames სიაში.
გამოიყენეთ map, იმისთვის რომ თითოეულ სახელს წინ დაუწეროთ "Welcome". განახლებული შედეგი შეინახეთ სიაში სახელწოდებით greet_users.

5) შექმენით usernames მასივი. გამოიყენეთ filter, რომ filtered_users სიაში მხოლოდ შეინახოთ სახელები, რომელთა სიმბოლოების რაოდენობაც 5-ს აღემატება.

6) map მეთოდის გამოყენებით numbers მასივში არსებული თითო ელემენტი გადაამრავლეთ 2 - ზე, და გამოიტანეთ ახალი მასივი ისეთი მნიშვნელობებით, რომლებმაც მოცემული ოპერაცია გაიარეს.

7) findIndex მეთოდის გამოყენებით console - ში დააბრუნეთ ისეთი რიცხვის index - რომელიც მეტია 3 - ზე.

8) numbers მასივი გაფილტრეთ ისეთი რიცვებისგან, რომლებიც მეტია 5 - ზე, შემდეგ გაატარეთ findIndex მეთოდში და გამოიტანეთ იმ რიცხვის index, რომელიც 3-ის ნამრავლია.

*/



// 2) 

const number = [10, 12, 13, 15, 23, 12, 33, 66, 0];
const even = number.filter(evenNum => {return evenNum % 2 == 0});

console.log(even);

// filter() არ ცვლის ორიგინალ მასივს.
// filter() აბრუნებს ახალ მასივს, რომელშიც მხოლოდ პირობის

// 3) 

const names = ['mariami', 'lika', 'sally', 'anamaria', 'anna'];
const startsWith = names.map(name => {return name[0].toUpperCase();});

console.log(startsWith);

// map() აბრუნებს ახალ მასივს და არ ცვლის ორიგინალ მასივს.
// name[0] იღებს სახელის პირველ ასოს.
// toUpperCase() პირველ ასოს დიდ ასოდ აქცევს.

// 4) 

const usernames = ['Mari', 'Maria', 'Lizi', 'lika', 'sally', 'Mira'];
const greet_users = usernames.map(username => {return 'Welcome' + ' ' + username});

console.log(greet_users);

// 5) 

const usernames1 = ['Mari', 'Lika', 'Salome', 'Anastasia', 'Annamaria', 'Bella'];
const filtered_users = usernames1.filter(user => {return user.length > 5});

console.log(filtered_users);

// 6) 

const numbers = [12, 13, 11, 55, 19, 14, 22, 24];
const dabled = numbers.map(number => {return number *  2})

console.log(dabled)


// 7) findIndex მეთოდის გამოყენებით console - ში დააბრუნეთ ისეთი რიცხვის index - რომელიც მეტია 3 - ზე.

const indexs = [1, 3, 4, 5, 6, 7, 9, 8, 10];
const chakeIndex = indexs.findIndex(i => {return i > 3;});

console.log(chakeIndex);


// 8)

const numbers2 = [10, 12, 13, 15, 23, 12, 33, 66, 0];

const filteredNumbers = numbers2.filter(num => {
    return num > 5;
});

const index = filteredNumbers.findIndex(num => {
    return num % 3 === 0;
});

console.log(index);

// filter() ტოვებს მხოლოდ 5-ზე მეტ რიცხვებს.
// findIndex() პოულობს პირველი ისეთი რიცხვის ინდექსს,
// რომელიც 3-ზე უნაშთოდ იყოფა.
// ინდექსების ათვლა იწყება 0-დან.
// გაფილტრული მასივია [10, 12, 13, 15, 23, 12, 33, 66].
// პირველი 3-ის ჯერადი რიცხვია 12, რომლის ინდექსია 1.
// ამიტომ console-ში დაიბეჭდება 1.