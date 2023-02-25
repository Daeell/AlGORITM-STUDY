function solution(A, B) {
    var answer = 0;
    A.sort((a,b) => a-b);
    B.sort((a,b) => a-b);
    var B_s=0;
    for (let i =0; i<A.length;i++){
        for(let j=B_s; j<B.length;j++){
            if (A[i]<B[j]){
                answer++;
                B_s = j+1;
                break;
            } 
        }
        
    }
    return answer;
}

console.log(solution([5,1,3,7], [2,2,6,8]))