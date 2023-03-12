function solution(number, k) {
    var answer = [];

    number = number.split('').reverse();
    while(number.length){
        let temp = number.pop();

        if (answer.length === 0){
            answer.push(temp)
        } else {
            while (k>0 && answer.length >0 && answer[answer.length -1]< temp){
                answer.pop();
                k--;
            }
            answer.push(temp);
        }
    }

    if(k !== 0){
        answer = answer.slice(0,-k);
    }

    return answer.join("");
}

console.log(solution("4185410000", 4))