// dfs, bfs 다 까먹었어요 ..! 우하하
var begin = "hit";
var target = "cog";
const words = ["hot", "dot", "dog", "lot", "log", "cog"];

function solution(begin, target, words) {
    var answer = 0;
    var count = 0;

    if (!words.includes(target)) {
        return 0;
    } else {
        for (let item of words) {
            for (let i = 0; i < len; i++) {
                if (begin[i] !== item[i]) {
                    count++;
                }
            }
        }
    }

    return answer;
}

console.log(solution(begin, target, words));
