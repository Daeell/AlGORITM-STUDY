const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().split("\n");

const str = input[0];
const boomStr = input[1];

const stk = [];

for (let i = 0; i < str.length; i++) {
  stk.push(str[i]);
  loop:
  while (stk.length >= boomStr.length) {
    for (let j = 0; j < boomStr.length; j++) {
      if (boomStr[j] !== stk[stk.length-boomStr.length+j]) {
        break loop;
      }
    }
    for (let j = 0; j < boomStr.length; j++) {
      stk.pop()
    }
  }
}

const answer = stk.length ? stk.join('') : 'FRULA';
console.log(answer);