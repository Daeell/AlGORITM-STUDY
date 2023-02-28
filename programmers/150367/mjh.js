// RangeError: Maximum call stack size exceeded
function binaryStringify (n) {
  let binString = n.toString(2);
  if (binString.length % 2 == 0) {
      binString = '0'+binString;
  }
  return binString;
}

function checkBT (str) {
  const checker = (left, right) => {
      if (right-left === 0) {
          return true;
      }
      let mid = (left+right)/2
      if (str[mid] === '0') {
          return false;
      }
      if (checker(left, mid-1) && checker(mid+1, right)) {
          return true;
      }
      return false;
  }
  return checker(0, str.length-1);
}

function solution(numbers) {
  let answer = [];
  numbers.map((n) => {
      let binString = binaryStringify(n);
      answer.push(+checkBT(binString));
      console.log(binString);
  })
  return answer;
}