/* 

1) შექმენით კონსტანტა სადაც შეინახავთ 10 - 100 ჩათვლით რიცხვს, თქვენი დავალებაა, რომ შეამოწმოთ მოსწავლის ქულა და შესაბამისად გამოიტანოთ შეფასება, მაგალითად, თუ მოსწავლის ქულა მეტია ან ტოლი 90 მაშინ გამოიტანეთ მნიშვნელობა 'A' 

2) მეორე დავალების გაკეთება სცადეთ ამჯერად switch - ის გამოყენებით, მოიძიეთ ინფორმაცია და კომენტარების სახით ახსენით მისი დანიშნულება

3) შექმენით ორი კონსტანტა სადაც შეინახავთ სახელს და ასაკს, თქვენი დავალებაა, რომ შეამოწმოთ უდრის თუ არა მომხმარებლის სახელი თქვენს სახელს და უდრის თუ არა მომხმარებლის ასაკი თქვენს ასაკს, თუ მოცემული პირობა არის true, გამოიტანეთ ტექსტი 'We have the same name or age' სხვა შემთხვევაში კი გამოიტანეთ ტექსტი "We don't have the same name and age", ამისათვის გამოიყენეთ logical operator 

4) შექმენით ორი კონსტანტა, პირველი age რომელშიც შეინახავთ ასაკს, მეორე hasTicket - რომელშიც შეინახავთ boolean მნიშვნელობას, თქვენი დავალებაა, რომ შეამოწმოთ იმ შემთხვევაში თუ მომხმარებლის ასაკი მეტია 15 - ზე და hasTicket - ის მნიშვნელობა არის true, მაშინ გამოიტანეთ ტექსტი 'You can go in, and watch a movie' სხვა შემთხვევაში "You can't go in", გამოიყენეთ logical, comparation operator - ები

5) შექმენით კონსტანტა temperature სადაც შეინახავთ ტემპერატურას, თქვენი დავალებაა ternary operator-ის გამოყენებით შეამოწმოთ თუ ტემპერატურა მეტია ან ტოლია 20 - ის მაშინ გამოიტანოთ 'It is warm', სხვა შემთხვევაში კი გამოიტანეთ 'It is cold'

*/

// 1)

const score = 95;

if (score >= 90) {
    console.log("A");
} else if (score >= 80) {
    console.log("B");
} else if (score >= 70) {
    console.log("C");
} else if (score >= 60) {
    console.log("D");
} else {
    console.log("F");
}


// 2)

// switch ამოწმებს ერთ მნიშვნელობას სხვადასხვა შესაძლო მნიშვნელობასთან.
// case განსაზღვრავს კონკრეტულ შემთხვევას.
// break აჩერებს switch-ს შესაბამისი case-ის შესრულების შემდეგ.
// default სრულდება მაშინ, როდესაც არცერთი case არ დაემთხვევა.

const grade = "A";

switch (grade) {
    case "A":
        console.log("Excellent!");
        break;
    case "B":
        console.log("Very good!");
        break;
    case "C":
        console.log("Good!");
        break;
    case "D":
        console.log("Needs improvement.");
        break;
    case "F":
        console.log("Failed.");
        break;
    default:
        console.log("Invalid grade.");
}


// 3)

const myName = "Mari";
const myAge = 15;

const userName = "Mari";
const userAge = 15;

if (userName === myName || userAge === myAge) {
    console.log("We have the same name or age");
} else {
    console.log("We don't have the same name and age");
}


// 4)

const age = 16;
const hasTicket = true;

if (age > 15 && hasTicket === true) {
    console.log("You can go in, and watch a movie");
} else {
    console.log("You can't go in");
}

// 5)

const temperature = 25;

const result = temperature >= 20
    ? "It is warm"
    : "It is cold";

console.log(result);