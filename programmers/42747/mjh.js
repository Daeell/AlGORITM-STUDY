// PASSED

function solution(citations) {
  var answer = 0;
  
  citations.sort((a,b) => a-b);
  
  if (citations[0] > citations.length)
      return citations.length;
  
  for (let i = citations.length-1; i > 0; i--) {
      if (citations.length - i <= citations[i] &&
          citations.length - i >= citations[i-1]) {
          answer = citations.length - i;
          break;
      }
  }
  
  return answer;
}