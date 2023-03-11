// PASSED

function solution(n, left, right) {
  let answer = [];
  
  for (let i = Math.floor(left/n)+1; i <= Math.floor(right/n)+1; i++) {
      for (let j = 1; j <= n; j++) {
          if ((i-1)*n + (j-1) < left || (i-1)*n + (j-1) > right) continue;
          i <= j ? answer.push(j) : answer.push(i);
      }
  }
  
  return answer;
}