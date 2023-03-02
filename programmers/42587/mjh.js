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

function solution(priorities, location) {
  const myPriority = priorities[location];

  const queue = new Queue();
  const leftDocsQueue = new Queue();
  const copyOfPriorities = [];

  const mineMineMineMineMineMineMineMineMineMineMine =
    "내 문서다. 건들지 마라.";

  priorities.map((priority, index) => {
    // Make copy of the priorities array.
    copyOfPriorities.push(priority);

    // Enqueue to queue object. This will be assumed as printer's waiting queue.
    if (index === location) {
      // Mark "THiS iS mY DOcuMeNT".
      queue.enqueue(mineMineMineMineMineMineMineMineMineMineMine);
    } else {
      queue.enqueue(priority);
    }
  });

  // Sort array by descending order and enqueue to queue object.
  // Head value of this queue will be a highest priority.
  copyOfPriorities.sort((a, b) => b - a);
  copyOfPriorities.map((value) => {
    leftDocsQueue.enqueue(value);
  });

  let cnt = 1;

  // Loop until value can be printed.
  while (queue.len) {
    const value = queue.dequeue();

    if (value === mineMineMineMineMineMineMineMineMineMineMine) {
      if (leftDocsQueue.watchHead() <= myPriority) {
        return cnt;
      } else {
        queue.enqueue(value);
        continue;
      }
    }

    if (leftDocsQueue.watchHead() <= value) {
      leftDocsQueue.dequeue();
      cnt++;
    } else {
      queue.enqueue(value);
    }
  }

  // Should Never Reached.
  return 0;
}
