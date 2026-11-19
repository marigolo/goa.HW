// 2
let isEven = function (num) {
  if (num % 2 == 0) {
    return true;
  } else {
    return false;
  }
};

console.log(isEven(20));
console.log(isEven(23));

// 3
let findMax = function (a, b) {
  if (a > b) {
    return a;
  } else if (a < b) {
    return b;
  } else {
    return a;
  }
};

console.log(findMax(2, 3));

// 4
let reverseString = function (str) {
  let result = '';

  for (let i = str.length - 1; i >= 0; i--) {
    result += str[i];
  }

  return result;
};

console.log(reverseString('Hello'));

// 5
let countVowels = function (str) {
  let count = 0;

  for (let i = 0; i < str.length; i++) {
    let letter = str[i].toLowerCase();

    if (
      letter == 'a' ||
      letter == 'e' ||
      letter == 'i' ||
      letter == 'o' ||
      letter == 'u'
    ) {
      count++;
    }
  }

  return count;
};

console.log(countVowels('Hi i am learning JS' ));

// 6
let getEvenNumbers = function (arr) {
  let evenNumbers = arr.filter(function (num) {
    return num % 2 == 0;
  });

  return evenNumbers;
};

console.log(getEvenNumbers([1, 2, 4, 5, 6, 6, 7]));

// 7
let factorial = function (n) {
  let result = 1;

  for (let i = 1; i <= n; i++) {
    result *= i;
  }

  return result;
};

console.log(factorial(5));

// 8

let isPalindrome = function (str) {
  return str === str.split('').reverse().join('');
};

// let isPalindrome = function(str) {
//     let reversed = '';

//     for (let i = str.length - 1; i >= 0; i--) {
//         reversed += str[i];
//     }

//     if (str === reversed) {
//         return true;
//     } else {
//         return false;
//     }
// };

console.log(isPalindrome('hello'));
console.log(isPalindrome('LEVEL'));

// 9
let findLongestWord = function (sentence) {
  let max = '';
  let word = '';

  for (let i = 0; i <= sentence.length; i++) {
    if (sentence[i] != ' ' && i < sentence.length) {
      word += sentence[i];
    } else {
      if (word.length > max.length) {
        max = word;
      }

      word = '';
    }
  }

  return max;
};

console.log(findLongestWord('I love programming'));

// 10
let getUniqueValues = function (arr) {
  return [...new Set(arr)];
};

console.log(getUniqueValues([1, 2, 2, 3, 4, 4]));

// 11
let capitalizeWords = function (sentence) {
  return sentence
    .split(' ')
    .map(function (word) {
      return word[0].toUpperCase() + word.slice(1);
    })
    .join(' ');
};

console.log(capitalizeWords('hello world'));

// 12
let areAnagrams = function (str1, str2) {
  str1 = str1.toLowerCase();
  str2 = str2.toLowerCase();

  if (str1.length !== str2.length) {
    return false;
  }

  for (let i = 0; i < str1.length; i++) {
    let count1 = 0;
    let count2 = 0;

    for (let j = 0; j < str1.length; j++) {
      if (str1[i] === str1[j]) {
        count1++;
      }

      if (str1[i] === str2[j]) {
        count2++;
      }
    }

    if (count1 !== count2) {
      return false;
    }
  }

  return true;
};

console.log(areAnagrams('listen', 'silent'));
