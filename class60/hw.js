// 2)

let fruits = ['Apple', 'Orange', 'Grape', 'Peach', 'Banana'];
let lenOfFruits = fruits.length;
console.log(`მასივში არის ${lenOfFruits} ელემენტი`);


// 3)

let todoList = [];
todoList.push('learn');
todoList.push('workout');
todoList.push('rest');
console.log(todoList);


// 4)

let numbers = [10, 20, 30, 40, 50];
let removedNumber = numbers.pop();
console.log(removedNumber);


// 5)

let colors = ["წითელი", "მწვანე", "ლურჯი", "ყვითელი", "იასამნისფერი"];
console.log(colors.at(0), colors.at(colors.length -1));


// 6)

let queue = ["გიორგი", "ანა", "ნიკა", "მარიამი"];
queue.shift();
console.log(queue);


// 7)

let frontEnd = ["HTML", "CSS", "JS"];
let backEnd = ["Node.js", "Python"];
let fullStack = frontEnd.concat(backEnd);
console.log(fullStack);


// 8)

let animals = ["Dog", "Cat", "Bear", "Wolf"];
console.log(animals.indexOf('Cat'));
console.log(animals.indexOf('lion'));
// -1, რადგან "lion" მასივში არ არსებობს


// 9)

let days = ["ორშაბათი", "სამშაბათი", "ოთხშაბათი", "ხუთშაბათი", "პარასკევი", "შაბათი", "კვირა"];
let workDays = days.slice(0, 5);
console.log(workDays);


// 10)

let randomMovies = ["Inception", "Interstellar"];
randomMovies.unshift('The Dark Knight');
console.log(randomMovies);


// 11)

let scores = [50, 65, 78, 92, 45, 88, 99];
let lastThree = scores.slice(4, 7);
console.log(lastThree);


// 12)

let searchHistory = [];

searchHistory.push('google.com');
searchHistory.push('github.com');
searchHistory.push('youtube.com');
searchHistory.pop();
searchHistory.push('stackoverflow.com');
console.log(searchHistory.length);
console.log(searchHistory.at(searchHistory.length -1));


// 13)

let shoppingList = ["bread", "milk", "cheese", "eg"];
console.log(shoppingList.indexOf('cheese'));