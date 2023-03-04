// PASSED... 설명이 불친절한 문제...
function binaryStringify(n) {
  let binString = n.toString(2);
  let i = 2;
  while (i < binString.length+1) {
    i *= 2;
  }
  while (binString.length < i-1) {
    binString = "0" + binString;
  }
  return binString;
}

function checkBT(str) {
  const checker = (left, right) => {
    if (right - left === 0) {
      return true;
    }
    let mid = (left + right) / 2;
    if (str[mid] === "0") {
      let i = left;
      while (i <= right) {
        if (str[i] === "1") {
          return false;
        }
        i++;
      }
      return true;
    }
    if (checker(left, mid - 1) && checker(mid + 1, right)) {
      return true;
    }
    return false;
  };
  return checker(0, str.length - 1);
}

function solution(numbers) {
  let answer = [];
  numbers.map((n) => {
    let binString = binaryStringify(n);
    answer.push(+checkBT(binString));
  });
  return answer;
}
