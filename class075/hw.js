// 2)

function userAge(age = 1){
    if (age >= 18){
        return 'You are an adult'
    } else{
        return 'You are not an adult'
    };
};

console.log(userAge(22));
console.log(userAge(2));

// 3)  of — მასივის ელემენტებს სათითაოდ იღებს.

function countLetters(txt) {
    let count = 0;
    for (let letter of txt) {
        if (letter.toLowerCase() !== letter.toUpperCase()) {
            count++;
        }
    }
  
    return count;
}
console.log(countLetters('Hello'));

// 4) 

function sum(arr){
    let total = 0;
    for (let i = 0; i < arr.length; i++) {
        total += arr[i];
    }

    return total;
}

console.log(sum([1, 2, 3, 4, 5]))

// 5) 

function square(a){
    return a**2
}

console.log(square(3))

// 6) 

function namSquare(a = 1, b = 2, c = 3){
    return a**b*c
}

console.log(namSquare(2, 2, 1))

// 7)
 
// return — ფუნქვიაშივე აბრუნებს მნიშვნელობას რისი გამოყენებაც შეგვიძლია იმავე ფუნქვიაში.
// console.log() — გამოაქვს ინფორმაცია კონსოლში.

function sum(a, b) {
    return a + b;
}

console.log(sum(20 * 1));


function multiply(a, b) {
    console.log(a * b)
}

multiply()