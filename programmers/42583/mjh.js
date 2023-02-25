// PASSED
class Queue {
  constructor(bridge_length) {
    this._arr = Array.from({ length: bridge_length }, () => 0);
  }
  enqueue(item) {
    this._arr.push(item);
  }
  dequeue() {
    return this._arr.shift();
  }
  len() {
    return this._arr.length;
  }
  watch(idx) {
    return this._arr[idx];
  }
}

function solution(bridge_length, weight, truck_weights) {
  let answer = 0;
  let queue = new Queue(bridge_length);
  let currentWeight = 0;
  let trucksLength = truck_weights.length;
  let i = 0;

  while (i < trucksLength) {
    while (currentWeight - queue.watch(0) + truck_weights[i] > weight) {
      currentWeight -= queue.dequeue();
      queue.enqueue(0);
      answer++;
    }
    currentWeight -= queue.dequeue();
    currentWeight += truck_weights[i];
    queue.enqueue(truck_weights[i]);

    // Advance.
    answer++;
    i++;
  }

  while (currentWeight > 0) {
    currentWeight -= queue.dequeue();
    answer++;
  }

  return answer;
}
