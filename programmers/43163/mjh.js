// PASSED
class Queue {
  constructor () {
      this._arr = [];
  }
  enqueue (item) {
      this._arr.push(item);
  }
  dequeue () {
      return this._arr.shift();
  }
  len () {
      return this._arr.length;
  }
}

function solution(begin, target, words) {
  let answer = 0;
  const wordLen = words[0].length;
  
  let graph = {};
  words.map((word1) => {
      words.map((word2) => {
          let cnt = 0;
          for (let i = 0; i < wordLen; i++) {
              if (word1[i] !== word2[i]) {
                  cnt++;
                  if (cnt > 1) {
                      break;
                  }
              }
          }
          if (cnt === 1) {
              if (!graph[word1]) {
                  graph[word1] = {};
              }
              if (!graph[word2]) {
                  graph[word2] = {};
              }
              graph[word1][word2] = 1;
              graph[word2][word1] = 1;
          }
      })
  })
  
  let queue = new Queue();
  let visited = {}
  
  words.map((word) => {
      let cnt = 0;
      for (let i = 0; i < begin.length; i++) {
          if (begin[i] !== word[i]) {
              cnt++;
          }
      }
      if (cnt === 1) {
          queue.enqueue([word, 1]);
          visited[word] = true;
      }
  })
  
  while (queue.len() > 0) {
      const [word, cnt] = queue.dequeue();
      if (word === target) {
          answer = cnt;
          break;
      }
      for (let word2 in graph[word]) {
          if (!visited[word2]) {
              visited[word2] = true;
              queue.enqueue([word2, cnt+1]);
          }
      }
  }
  
  return answer;
}