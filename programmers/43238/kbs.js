function solution(n, times){
	times.sort((a, b) => {
		return a - b;})
    let left = 1;
    let right = n * (times[times.length - 1]);
    let answer = right;
    
    while(left <= right){
    	let mid = parseInt((left + right) / 2);
        let cnt = 0;
        times.forEach(value => {
        	cnt += parseInt(mid / value);
            if(cnt >= n){
            	answer = Math.min(answer , mid);
            }
        });
        if(cnt >= n){
			right = mid - 1;
        }
        else{
        	left = mid + 1;
        }
    }
    return answer
}