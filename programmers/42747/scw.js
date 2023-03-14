function solution(citations) {
    var answer = 0;
    var dic ={};
    
    for (let i=0; i<Math.max(...citations);i++){
        for(let j=0; j<citations.length; j++){
            if (i<= citations[j]){
                if(dic[i]===undefined){
                    dic[i]=1;
                } else{
                    dic[i]++;
                }
            }
        }
    }
    
    for(let k = Math.max(...citations);k>=0;k--){
        if(dic[k]>=k){
            answer = k;
            break;
        }
    }
    return answer;
}


console.log(solution([3, 0, 6, 1, 5]))