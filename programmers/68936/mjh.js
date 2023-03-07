// PASSED

function solution(arr) {
  let answer = [];
  
  function recur(row, col, len) {
      let cnt0 = 0;
      let cnt1 = 0;
      loop:
      for (let i = row; i < row+len; i++) {
          for (let j = col; j < col+len; j++) {
              if (arr[i][j] === 0) {
                  cnt0++;
              } else {
                  cnt1++;
              }
              if (cnt0 && cnt1) {
                  break loop;
              }
          }
      }
      if (!(cnt0 && cnt1)) {
          return [cnt0/len**2, cnt1/len**2];
      } else {
          let retCnt0 = 0;
          let retCnt1 = 0;
          for (let i = 0; i < 2; i++) {
              for (let j = 0; j < 2; j++) {
                  let tmp = recur(row+(len/2*i), col+(len/2*j), len/2);
                  retCnt0 += tmp[0];
                  retCnt1 += tmp[1];
              }
          }
          return [retCnt0, retCnt1];
      }
  }
  
  answer = recur(0, 0, arr.length);
  
  return answer;
}