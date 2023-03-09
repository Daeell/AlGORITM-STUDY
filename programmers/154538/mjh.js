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

function solution(x, y, n) {
    let answer = -1;
    
    const queue = new Queue();
    const visited = new Set();
    
    queue.enqueue([x, 0]);
    visited.add(x);
    
    while (queue.head) {
        const [num, cnt] = queue.dequeue();
        
        if (num > y**2) {
            break;
        }

        if (num === y) {
            answer = cnt;
            break;
        }
        if (!visited.has(num+n)) {
            visited.add(num+n);
            queue.enqueue([num+n, cnt+1]);
        }
        if (!visited.has(num*2)) {
            visited.add(num*2);
            queue.enqueue([num*2, cnt+1]);
        }
        if (!visited.has(num*3)) {
            visited.add(num*3);
            queue.enqueue([num*3, cnt+1]);
        }
    }
    
    return answer;
}