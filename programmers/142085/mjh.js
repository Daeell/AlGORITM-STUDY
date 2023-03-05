// PASSED

class MaxHeap {
  constructor() {
      this._arr = [null];
  }
  heappush(value) {
      const arr = this._arr;
      arr.push(value);
      let idx = arr.length - 1;
      while (idx > 1) {
          const parentIdx = Math.floor(idx/2);
          if (arr[parentIdx] < arr[idx]) {
              const tmp = arr[parentIdx];
              arr[parentIdx] = arr[idx];
              arr[idx] = tmp;
              idx = parentIdx;
          } else {
              break;
          }
      }
  }
  heappop() {
      const arr = this._arr;
      if (arr.length === 1) {
          return null;
      }
      if (arr.length === 2) {
          return arr.pop();
      }
      const returnValue = arr[1];
      
      arr[1] = arr.pop();
      let idx = 1;
      while (arr[idx*2] !== undefined) {
          let childIdx = (arr[idx*2+1] !== undefined && arr[idx*2] < arr[idx*2+1]) ? idx*2+1 : idx*2;
          if (arr[idx] < arr[childIdx]) {
              const tmp = arr[childIdx];
              arr[childIdx] = arr[idx];
              arr[idx] = tmp;
              idx = childIdx;
          } else {
              break;
          }
      }
      
      return returnValue;
  }
  length() {
      return this._arr.length - 1;
  }
}

function solution(n, k, enemy) {
  let answer = 0;
  
  const heap = new MaxHeap();
  for (let i = 0; i < enemy.length; i++) {
      n -= enemy[i];
      heap.heappush(enemy[i]);
      while (k > 0 && n < 0) {
          n += heap.heappop()
          k--;
      }
      if (k === 0 && n < 0) {
          break;
      }
      answer++;
  }
  
  return answer;
}