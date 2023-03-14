function solution(n, s) {
    if(n>s){
        return [-1];
    }
    
    let min_val = Math.floor(s%n);
    const answer = Array(n).fill(Math.floor(s/n))
    let idx = answer.length -1
    
    while (min_val>0){
        answer[idx--]++;
        min_val--;
    }
    
    return answer;
}

console.log(solution(2, 9))