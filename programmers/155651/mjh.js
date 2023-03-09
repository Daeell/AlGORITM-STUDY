// PASSED

class MinHeap {
  constructor() {
      this._arr = [null];
  }
  heappush(value) {
      const arr = this._arr;
      arr.push(value);
      let idx = arr.length - 1;
      while (idx > 1) {
          const parentIdx = Math.floor(idx/2);
          if (arr[parentIdx] > arr[idx]) {
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
          let childIdx = (arr[idx*2+1] !== undefined && arr[idx*2] > arr[idx*2+1]) ? idx*2+1 : idx*2;
          if (arr[idx] > arr[childIdx]) {
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

function solution(book_time) {
    let answer = 0;
    
    const timeArr = [];
    
    book_time.map((data) => {
        const start = data[0].split(':');
        const end = data[1].split(':');
        timeArr.push([(+start[0])*60 + (+start[1]), (+end[0])*60 + (+end[1]) + 10])
    });
    
    timeArr.sort((a,b) => a[0]-b[0]);
    console.log(timeArr);
    
    const heap = new MinHeap();
    let roomCnt = 0;
    
    timeArr.map(([start, end]) => {
        
        let earliestEndTime = heap.heappop() ?? 1440;

        while (earliestEndTime !== 1440 && earliestEndTime < start) {
            earliestEndTime = heap.heappop();
            roomCnt--;
        }
        
        if (earliestEndTime > start) {
            heap.heappush(earliestEndTime);
            roomCnt++;
        }
        
        heap.heappush(end);
        
        answer = answer < roomCnt ? roomCnt : answer;
        
    })
    
    return answer;
}