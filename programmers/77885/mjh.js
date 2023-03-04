// PASSED
function solution(numbers) {
    let answer = [];
    
    numbers.map((num) => {
        if (num === 1) {
            // 1일때는 아래 공식으로 해결되지 않으므로 예외처리...
            answer.push(2);
        } else {
            const binaryString = num.toString(2);

            if (binaryString[binaryString.length - 1] === '0') {
                answer.push(num + 1);
            } else if (binaryString[binaryString.length - 2] === '0') {
                answer.push(num + 1);
            } else {
                let index = binaryString.length - 3;
                let i = 2;
                while (index >= 0) {
                    if (binaryString[index] === '0') {
                        break;
                    }
                    i++;
                    index--;
                }
                answer.push(num + (2 ** (i - 1)));
            }
        }
    })
    
    return answer;
}