// PASSED
function solution(numbers) {
  let answer = Array.from({ length: numbers.length }, () => -1);
  let stack = [];

  for (let i = numbers.length - 1; i > -1; i--) {
    while (stack.length > 0 && stack.at(-1) <= numbers[i]) {
      stack.pop();
    }
    answer[i] = stack.length > 0 ? stack.at(-1) : answer[i];
    stack.push(numbers[i]);
  }

  return answer;
}
