// PASSED

function solution(numbers) {
  let answer = '';
  
  function compare(a, b) {
      a = '' + a + a;
      b = '' + b + b;
      
      let i = 0;
      while (i < a.length && i < b.length) {
          if (+a[i] > +b[i]) {
              return -1;
          } else if (+a[i] < +b[i]) {
              return 1;
          }
          i++;
      }
      
      return 0;
  }
  
  numbers.sort(compare);
  
  if (numbers[0] === 0) {
      return '0';
  }
  
  numbers.map((num) => {
      answer += num;
  })
  
  return answer;
}