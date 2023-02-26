// PASSED
function solution(n, computers) {
  const findRoot = (num) => {
    if (arr[num] !== num) {
      arr[num] = findRoot(arr[num]);
    }
    return arr[num];
  };

  let answer = 0;

  let arr = Array.from({ length: n }, (v, i) => i);

  const computersLen = computers.length;
  for (let i = 0; i < computersLen; i++) {
    for (let j = 0; j < computersLen; j++) {
      if (i === j || computers[i][j] === 0) continue;
      arr[findRoot(i)] = arr[findRoot(j)];
    }
  }

  arr.map((value, idx) => {
    if (value === idx) answer++;
  });

  return answer;
}
