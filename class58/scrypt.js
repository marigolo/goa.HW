// let age = 23
// let mesige = age > 18 ? 'old enaugth' : 'minor';

// switch (athleteFinalPosition) {
//   case 'first place':
//     console.log('You get the gold medal!');
//     break;

//   case 'second place':
//     console.log('You get the silver medal!');
//     break;

//   case 'third place':
//     console.log('You get the bronze medal!');
//     break;

//   default:
//     console.log('No medal awarded.');
//     break;
// }

//EcmaScript - არის js-ის განახლება
// ES6 - EcmaScript- ის მე6 ვერსია რომლის შემდეგაც js-ს დაემატა  let, const და კიდევ ბევრი რამ გამოვიდა 2015 წელს

let name = "";
let nickname;

if (name) {
  nickname = name;
} else {
  nickname = "stranger";
}

let day = 5;

switch (day) {
  case 1:
    console.log("Monday");
    break;

  case 2:
    console.log("Tursday");
    break;

  case 3:
    console.log("wadnasday");
    break;

  case 4:
    console.log("Thursday");
    break;

  case 5:
    console.log("Friday");
    break;

  case 6:
    console.log("Daturday");
    break;

  case 7:
    console.log("Sunday");
    break;

  default:
    console.log("invalid day");
    break;
}
