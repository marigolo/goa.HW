// 2)

let even = function isEven(num) {
  if (num % 2 == 0) {
    return true;
  } else {
    return false;
  }
};

console.log(even(20));
console.log(even(23));

// 3)

let max = function findMax(a, b) {
  if (a > b) {
    return a;
  } else if (a < b) {
    return b;
  } else {
    return 'ტოლებია';
  }
};

console.log(max(2, 3));

// 4)

function reverseString(str) {
  let result = '';

  for (let i = str.length - 1; i >= 0; i--) {
    result += str[i];
  }

  return result;
}

console.log(reverseString('Hello'));

// 5)

let Vowels = function countVowels(str) {
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

console.log(Vowels('Hi i am learning JS'));

// 6)

let enen1 = function getEvenNumbers(arr) {
  let evenNumbers = arr.filter((num) => num % 2 == 0);
  return evenNumbers;
};

console.log(enen1([1, 2, 4, 5, 6, 6, 7]));

// 7)

let getFactorial = function factorial(n) {
  let ress = 1;

  for (let i = 1; i <= n; i++) {
    ress *= i;
  }

  return ress;
};

console.log(getFactorial(5));

// 8)

let findPalindrome = function isPalindrome(str) {
  return str === str.split('').reverse().join('');
};

console.log(findPalindrome('hello'));
console.log(findPalindrome('LEVEL'));

// 9)

let longest = function findLongestWord(sentence) {
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

console.log(longest('I love programming'));

// 10)

function getUniqueValues(arr) {
  return [...new Set(arr)];
}

console.log(getUniqueValues([1, 2, 2, 3, 4, 4]));

// 11)

let capitalize = function capitalizeWords(sentence) {
  return sentence
    .split(' ')
    .map((word) => word[0].toUpperCase() + word.slice(1))
    .join(' ');
};

console.log(capitalize('hello world'));

// 12)

function areAnagrams(str1, str2) {
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
}

console.log(areAnagrams('listen', 'silent'));
