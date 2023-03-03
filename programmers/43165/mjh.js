// PASSED
function solution(numbers, target) {
  let answer = 0;
  const lastIndex = numbers.length;
  
  function search(index, num) {
      if (index === lastIndex) {
          if (num === target) {
              answer++;
          }
          return;
      }
      search(index + 1, num - numbers[index]);
      search(index + 1, num + numbers[index]);
      return;
  }
  search(1, -numbers[0]);
  search(1, +numbers[0]);
  
  return answer;
}