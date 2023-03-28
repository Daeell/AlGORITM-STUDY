// 자바스크립트로 백준 풀지 말자... 입력 받기 너무 힘들다

const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().split("\n");

class Paper {
    constructor (x, y) {
        this._arr = Array.from({length: +x}, () => Array.from({length: +y}, () => 0));
    }

    fill (x1, y1, x2, y2) {
        const arr = this._arr;
        for (let i = +x1; i < +x2; i++) {
            for (let j = +y1; j < +y2; j++) {
                arr[i][j] = 1;
            }
        }
    }

    countEmptyArea () {
        const arr = this._arr;
        const retArr = [];
        const dx = [-1, 0, 0, 1];
        const dy = [0, -1, 1, 0];

        for (let i = 0; i < arr.length; i++) {
            for (let j = 0; j < arr[0].length; j++) {
                if (arr[i][j] === 0) {

                    const queue = [];
                    let ptr = 0;
                    let cnt = 0;

                    queue.push([i, j]);
                    arr[i][j] = 1;
                    while (ptr < queue.length) {
                        const [x, y] = queue[ptr++];
                        cnt++;
                        for (let k = 0; k < 4; k++) {
                            const xx = x+dx[k];
                            const yy = y+dy[k];
                            if (0 <= xx && xx < arr.length && 0 <= yy && yy < arr[0].length && arr[xx][yy] === 0) {
                                queue.push([xx, yy]);
                                arr[xx][yy] = 1;
                            }
                        }
                    }
                    retArr.push(cnt);
                }
            }
        }

        return retArr.sort((a, b) => a - b);
    }
}

const [M, N, K] = input[0].split(' ');
const paper = new Paper(N, M);
for (let i = 1; i <= K; i++) {
    const [a, b, c, d] = input[i].split(' ');
    paper.fill(a, b, c, d);
}

const retArr = paper.countEmptyArea();
console.log(`${retArr.length}\n${retArr.join(' ')}`);