// PASSED

function solution(n, s) {
  var answer = [];
  
  const baseNum = Math.floor(s/n);
  
  if (baseNum === 0) {
      return [-1];
  }
  
  const increasedNum = baseNum + 1;
  const increasedNumCnt = s - baseNum*n;
  
  for (let i = 0; i < n - increasedNumCnt; i++) {
      answer.push(baseNum);
  }
  for (let i = 0; i < increasedNumCnt; i++) {
      answer.push(increasedNum);
  }
  
  return answer;
}