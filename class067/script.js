/*
თუ გვინდა რომ ჩვენი კოდი ერთხელ მაინც გამოიტანოს  და მერე ამოწმებს ვიყენებთ - do , while - გამოაქვს ყველა იტერაცია

while - არასწორი რომც იყოს მაინც გამოიტანს do-ს


// brake - გაწყვეტს კოდს როცა კონდიშენი შესრულდება


iterators - .map(), filter(), forEach -მასივს გადაუვლიან

forEach- iRebs TiToeul elements
*/

// using  do , while

// let countString = '';
// let i = 0;

// do {
//   countString = countString + i;
//   i++;
// } while (i < 5);

// console.log(countString);


// Using brake

const rapperArray = ["Lil' Kim", "Jay-Z", "Notorious B.I.G.", "Tupac"];

for (let i = 0; i < rapperArray.length; i++) {
  console.log(rapperArray[i]);

  if (rapperArray[i] === "Notorious B.I.G.") {
    break;
  }
}

console.log("And if you don't know, now you know.");

for (let i = 10; i <= 50; i++){
    if (i === 25) {
        console.log(i)
    }

    console.log('found 25')
}

// using forEach

const artists = ['Emenem', 'the weeknd', 'JZ'];

artists.forEach((artist) => {
    console.log('i love: ' + artist);
});




/* CW 1*/


// 1) 

let i = 0;

do {
  console.log(i);
  i++;
} while (i <= 10);




// 2)

const mentors = ['random 1', 'random 2', 'Lika', 'random 3', 'random 4'];

for (let i = 0; i < mentors.length; i++) {
  if (mentors[i] === 'Lika') {
    break;
  };
};

console.log('Found a mentor: Lika');


// -------------- CW2 --------------

const favArtists = ['Emenem', 'the weeknd', 'JZ']

favArtists.forEach((artist) => {
    console.log('i listen to: ' + artist);
});