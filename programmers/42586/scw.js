function solution(progresses, speeds) {
    var answer = [];
    var temp = Array(progresses.length).fill(0);

    for (let i=0;i<progresses.length;i++){
        temp[i] = progresses[i]
    }

    while(temp.length>0){
        
        for (let i =0; i<temp.length; i++){
            temp[i] += speeds[i]
        }

        if (temp[0]>=100){
            let cnt =0;
            while (true){
                if (temp[0]>=100){
                    temp.shift();
                    speeds.shift();
                    cnt++;
                } else{
                    break;
                }
                
            }
            answer.push(cnt);
        }
    }
    
    return answer;
}

console.log(solution([93, 30, 55], [1, 30, 5]))