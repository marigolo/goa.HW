// 1) 1-დან 10-მდე რიცხვების დაბეჭდვა

let i = 1;

while (i <= 10) {
    console.log(i);
    i++;
}


// 2) 1-დან 100-მდე რიცხვების ჯამი

let num = 1;
let sum = 0;

while (num <= 100) {
    sum += num;
    num++;
}

console.log(sum);


// 3) რიცხვის გამრავლების ტაბულა 10-მდე

let number = 2;
let x = 1;

while (x <= 10) {
    console.log(number * x);
    x++;
}


// 4) მასივში არსებული ყველა ლუწი რიცხვის დაბეჭდვა

let numbers = [1, 4, 7, 8, 10, 13, 16];
let y = 0;

while (y < numbers.length) {
    if (numbers[y] % 2 === 0) {
        console.log(numbers[y]);
    }
    
    y++;
}


// 5) პაროლის შემოწმება

let correctPassword = "12345";
let password = prompt("შეიყვანე პაროლი:");

while (password !== correctPassword) {
    password = prompt("არასწორი პაროლი. სცადე თავიდან:");
}

console.log("სწორი პაროლია!");


// 6) მასივის თითოეული ელემენტის 2-ზე გამრავლება

let nums = [2, 4, 6, 8, 10];
let z = 0;

while (z < nums.length) {
    console.log(nums[z] * 2);
    z++;
}


// 7) მასივის თითოეული ელემენტის ნაშთი 3-ზე გაყოფისას

let list = [5, 7, 10, 14, 20];
let s = 0;

while (s < list.length) {
    console.log(list[s] % 3);
    s++;
}


// 8) ვარსკვლავების 5x5 კვადრატი

for (let i = 0; i < 5; i++) {
    let row = "";

    for (let j = 0; j < 5; j++) {
        row += "* ";
    }

    console.log(row);
}


// 9) გამრავლების სრული ტაბულა 1-დან 10-მდე

for (let i = 1; i <= 10; i++) {

    for (let j = 1; j <= 10; j++) {
        console.log(i + " x " + j + " = " + i * j);
    }

}


// 10) ორი მასივის საერთო ელემენტები

let arrayA = ["English", "Georgian", "French", "Russian"];
let arrayB = ["English", "Georgian", "German", "Russian"];

for (let i = 0; i < arrayA.length; i++) {

    for (let j = 0; j < arrayB.length; j++) {

        if (arrayA[i] === arrayB[j]) {
            console.log(arrayA[i]);
        }

    }
}


// 11)

let matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]];

let sums = 0;

for (let i = 0; i < matrix.length; i++) {

    for (let j = 0; j < matrix[i].length; j++) {
        sums += matrix[i][j];
    }

}

console.log(sums);