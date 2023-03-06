function solution(places) {
    var answer = [];

    function check_(place_arr, y, x, cnt){
        var direc = [[0,1],[0,-1],[1,0],[-1,0]]
        
        for(let i=0;i<4;i++){
            let ny = direc[i][0] + y;
            let nx = direc[i][1] + x;

            if(0<=nx && nx<5 && 0<=ny && ny<5){
                if(place_arr[ny][nx]==='P'){
                    cnt++;
                    if(cnt>=2) return false;
                }
            }
        }

        return true;
    }

    for(let place of places){
        let place_arr=[];
        let flag = true;
        
        for(let line of place){
            place_arr.push([...line])
        }
        
        check_len: for(let i=0;i<place_arr.length;i++){
            for(let j=0;j<place_arr[0].length;j++){
                if(place_arr[i][j]==='P'){
                    flag = check_(place_arr,i,j,1)
                    if(!flag) break check_len;
                }
                else if(place_arr[i][j]==='O') {
                    flag = check_(place_arr,i,j,0)
                    if(!flag) break check_len;
                }
            }
        }

        if(flag){
            answer.push(1);
        }else{
            answer.push(0);
        }
    }

    return answer;
}

console.log(solution([["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"]]))