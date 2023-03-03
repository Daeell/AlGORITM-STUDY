// 1,2번 케이스가 틀려요...
function solution(numbers) {
  let answer = [];
  
  numbers.map((num) => {
      const binaryString = num.toString(2);
              
      if (binaryString[binaryString.length - 1] === '0') {
          answer.push(num + 1);
      } else if (binaryString[binaryString.length - 2] === '0') {
          answer.push(num + 1);
      } else {
          let index = binaryString.length - 3;
          let i = 2;
          while (index >= 0) {
              if (binaryString[index] === '0') {
                  break;
              }
              i++;
              index--;
          }
          answer.push(num + (2 ** (i - 1)));
      }
      
  })
  
  return answer;
}