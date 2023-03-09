function solution(book_time) {
    var answer = [];
    var arr =[];
    for(let i=0; i<book_time.length; i++){
        let [s, e] = book_time[i];
        let [s_h, s_m] = s.split(":").map(Number)
        let [e_h, e_m] = e.split(":").map(Number)

        arr.push([s_h*60+s_m, e_h*60+e_m+10])
    }
    
    arr.sort((a,b) => a[0]-b[0]);
    
    for(let i=0;i<arr.length;i++){
        if(answer.length===0){
            answer.push(arr[i][1])
        } else{
            let flag = true;
            
            for(let j=0;j<answer.length;j++){
                if(arr[i][0]>= answer[j]){
                    answer[j]=arr[i][1]
                    break;
                } else if(j === answer.length-1){
                    flag = false;
                }
            }

            if(!flag){
                answer.push(arr[i][1])
            }

        }
    }
    
    return answer.length;
}

console.log(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))