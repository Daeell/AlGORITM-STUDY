const progresses = [93, 30, 55];
const speeds = [1, 30, 5];

function solution(progresses, speeds) {
    var answer = [];
    var day = [];
    // 개발: 남은 날짜를 구하는 법
    for (let i = 0; i < progresses.length; i++) {
        var cnt = 0;
        while (progresses[i] < 100) {
            progresses[i] += speeds[i];
            cnt += 1;
        }
        day.push(cnt);
    }

    // 배포: 같이 배포되는 친구 구하는 법
    let max = day[0];
    let count = 1;
    for (let i = 1; i < day.length; i++) {
        if (day[i] <= max) {
            count++;
        } else {
            max = day[i];
            answer.push(count);
            count = 1;
        }
    }
    answer.push(count);
    return answer;
}

console.log(solution(progresses, speeds));
