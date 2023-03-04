function solution(n, m, section) {
    var answer = 0;

    while(section.length>0){
        var s = section.shift();
        var e = s+m-1;
        while(true){
            if (section[0]<=e){
                section.shift();
            }
            else{
                answer++;
                break
            }
        }
    }

    return answer;
}


console.log(solution(8, 4, [2, 3, 6]))