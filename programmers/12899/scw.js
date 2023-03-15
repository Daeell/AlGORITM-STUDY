function solution(n) {
    var answer = '';
    
    while(n>0){
        if(n%3 === 0){
            answer +='4';
            n = Math.floor(n/3) -1;
        } else {
            answer +=(n%3).toString();
            n = Math.floor(n/3);
        }
    }
    answer = answer.split("").reverse().join("");

    return answer;
}

console.log(solution(1))

