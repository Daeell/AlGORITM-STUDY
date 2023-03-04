// PASSED
function solution(progresses, speeds) {
  let answer = [];
  let queue = []
  progresses.map((progress) => {
      queue.push(progress);
  })
  
  ptr = 0;
  while (ptr < queue.length) {
      cnt = 0;
      for (let i = ptr; i < queue.length; i++) {
          if (queue[i] >= 100) {
              cnt++;
              ptr++;
          } else {
              break;
          }
      }
      if (cnt > 0) {
          answer.push(cnt);
      }
      for (let i = ptr; i < queue.length; i++) {
          queue[i] += speeds[i];
      }
  }
  
  return answer;
}