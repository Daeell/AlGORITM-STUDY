function solution(n, times) {
    var answer = Number.MAX_SAFE_INTEGER;
    let maxi = times[times.length -1] *n;
    let mini =0;

    while (mini< maxi){
        let mid = Math.floor((mini+maxi)/2);
        let temp =0;
        for(let i=0;i<times.length;i++){
            temp += Math.floor(mid/times[i]);
        }
        if (temp>=n){
            answer = mid<answer ? mid : answer;
        }

        if (temp<n){
            mini = mid +1;
        } else {
            maxi = mid;
        }

    }
    return answer;
}

console.log(solution(6, [7, 10]))