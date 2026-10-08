// nested for loop:
/*
let bobsFollowers = ["Alice", "David", "Emma", "George"];
let tinasFollowers = ["Alice", "David", "Sophia"];
let mutualFollowers = [];

for (let i = 0; i < bobsFollowers.length; i++) {
  for (let j = 0; j < tinasFollowers.length; j++) {
    if (bobsFollowers[i] === tinasFollowers[j]) {
      mutualFollowers.push(bobsFollowers[i]);
    }
  }
}

------------- while loop ------------

let counter = 20; ცვლადს ვქმნით
while(counter <= 20) { ვაუბნები სადამდე უნდა გაჩერდეს
    console.log(counter) ვლოგავთ
    counter++ ყოველ იტერაციაზე ვამატებთ 1
}

------------- On words -------------


let word = "Hello";
let i = 0;

while (i < word.length) {
    console.log(word[i]);
    i++;
}
*/



// ---------------- CW1 ----------------

const languageA = ['English', 'Georgian', 'Frensh','Rassian', 'German'];
const languageB = ['English', 'Georgian', 'Turkish','Armenian', 'German'];

for(i = 0; i < languageA.length; i++) {
    for(x = 0; x < languageB.length; x++) {
        if(languageA[i] == languageB[x]){
            console.log(`found mutual language: ${x}`)
        };
        
    };
};

// ---------------- CW2 ----------------


let fruits = ['apple', 'cherry', 'melon'];
let curentFruet;

while(curentFruet != 'cherry' ) {
    curentFruet = fruits( Math.floor(math.random() *4));
    console.log(curentFruet);
};

