// PASSED

function solution(places) {
  const answer = [];
  
  function check(arr, x, y, depth) {
      const dx = [1, 0, 0, -1];
      const dy = [0, 1, -1, 0];
      let flag = true;
      
      for (let i = 0; i < 4; i++) {
          let xi = x+dx[i];
          let yi = y+dy[i];
          if (0 <= xi && xi < 5 && 0 <= yi && yi < 5) {
              if ((depth ? !(xi === depth[0] && yi === depth[1]) : true) && arr[xi][yi] === 'P') {
                  return false;
              } else if (!depth && arr[xi][yi] === 'O') {
                  flag = check(arr, xi, yi, [x, y]) || false;
                  if (!flag) return false;
              }
          }
      }
      return true;
  }
  
  places.map(arr => {
      let flag = true;
      loop:
      for (let i = 0; i < 5; i++) {
          for (let j = 0; j < 5; j++) {
              if (arr[i][j] === 'P') {
                  flag = check(arr, i, j, 0) || false;
                  if (!flag) break loop;
              }
          }
      }
      flag ? answer.push(1) : answer.push(0);
  })
  
  return answer;
}