// PASSED

class Node {
  constructor(value) {
    this.next = null;
    this.value = value;
  }
}

class Queue {
  constructor() {
    this.head = null;
    this.tail = null;
    this.len = 0;
  }

  enqueue(value) {
    const newNode = new Node(value);

    if (this.head === null) {
      this.head = newNode;
    } else {
      this.tail.next = newNode;
    }

    this.tail = newNode;
    this.len++;
  }

  dequeue() {
    if (this.head === null) {
      return null;
    }

    let value = this.head.value;

    if (this.head === this.tail) {
      this.head = null;
      this.tail = null;
    } else {
      this.head = this.head.next;
    }

    this.len--;

    return value;
  }

  watchHead() {
    return this.head ? this.head.value : null;
  }
}

function solution(n, wires) {
    let answer = 10**10;
    
    const graph = {}
    for (let i = 0; i < wires.length; i++) {
        const [v1, v2] = wires[i];
        if (!graph[v1]) {
            graph[v1] = {};
        }
        if (!graph[v2]) {
            graph[v2] = {};
        }
        graph[v1][v2] = 1;
        graph[v2][v1] = 1;
    }
    
    for (let i = 0; i < wires.length; i++) {
        const [v1, v2] = wires[i];
        graph[v1][v2] = 0;
        graph[v2][v1] = 0;
        
        const cntArr = [];
        const visited = new Set();
        
        for (let j = 1; j < n+1; j++) {
            let queue = new Queue();
            if (visited.has(j)) {
                continue;
            }
            queue.enqueue(j);
            visited.add(j);
            let cnt = 0;
            
            while (queue.len) {
                let vv1 = queue.dequeue();
                cnt++;
                
                for (let vv2 in graph[vv1]) {
                    if (graph[vv1][vv2] === 0) {
                        continue;
                    }
                    if (!visited.has(+vv2)) {
                        queue.enqueue(vv2);
                        visited.add(+vv2);
                    }
                }
            }
            cntArr.push(cnt);
        }
        const abs = cntArr[0] - cntArr[1] > 0 ? cntArr[0] - cntArr[1] : cntArr[1] - cntArr[0];
        answer = answer > abs ? abs : answer;
        
        graph[v1][v2] = 1;
        graph[v2][v1] = 1;
    }
    
    return answer;
}