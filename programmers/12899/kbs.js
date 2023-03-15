function solution(n) {
    const country124 = [4, 1, 2]; 
    var answer = '';
    
    while(n){
        answer = country124[n%3] + answer;
        n = (n%3 == 0)? n/3 -1 : Math.floor(n/3);
    }
    return answer;
}