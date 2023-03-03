function solution(priorities, location) {
    var answer = 0;
    var temp =[];
    var cnt=0;
    for(let i =0; i<priorities.length; i++){
        temp.push([i, priorities[i]])
    }
    console.log(temp)

    while(true){
        let [num, pri] = temp.shift();

        let arr = temp.filter(x => x[1]>pri)

        if(arr.length>0){
            temp.push([num,pri]);
        } else{
            cnt++;
            if (num === location){
                answer = cnt;
                break;
            }
            continue;
        }
    }
    

    return answer;
}

console.log(solution([1, 1, 9, 1, 1, 1], 0))