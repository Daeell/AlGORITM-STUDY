// PASSED
function solution(A, B) {
  let answer = 0;
  
  const numSortFunction = (a, b) => a - b
  
  A.sort(numSortFunction);
  B.sort(numSortFunction);
  
  let aIndex = A.length - 1;
  let bIndex = B.length - 1;
  while (bIndex > -1 && aIndex > -1) {
      if (A[aIndex] < B[bIndex]) {
          answer++
          aIndex--
          bIndex--
      }
      else {
          aIndex--
      }
  }
  
  return answer;
}