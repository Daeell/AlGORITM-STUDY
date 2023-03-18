// 주의 : 이 문제는 node.js로 푸는 것이 불가능한 문제입니다. (무조건 메모리 초과 남)

const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().split("\n");

const [N, K] = input[0].split(' ').map(v=>+v);

const dp = [];
for (let i = 0; i <= K; i++) {
  dp.push(0);
}
dp[0] = 1;

for (let i = 1; i < input.length; i++) {
  for (let j = input[i]; j <= K; j++) {
    dp[j] += dp[j - input[i]];
  }
}

console.log(dp[K]);
