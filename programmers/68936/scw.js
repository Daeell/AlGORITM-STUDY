function solution(arr) {
    var answer = [0,0];

    function check_num(arrr){
        const f_num = arrr[0][0];

        for(let i=0;i<arrr.length;i++){
            for(let j=0;j<arrr.length;j++){
                if (arrr[i][j] !== f_num){
                    return -1;
                }
            }
        }

        return f_num;
    }

    function cutter(array, x_s, x_e, y_s, y_e, len){
        let arr=Array.from(new Array(len), ()=>new Array(len));

        for(let i=y_s; i<y_e;i++){
            for(let j=x_s; j<x_e;j++){
                arr[i-y_s][j-x_s] = array[i][j];
            }
        }

        return arr
    }

    const recur = array =>{
        let value = check_num(array);

        if (value === 0){
            answer[0] +=1;
        } else if (value === 1){
            answer[1] +=1;
        } else{
            const div = parseInt(array.length/2);

            let first = cutter(array, 0, div, 0, div, div); // 1사분면
            let second = cutter(array, div, div*2, 0, div, div); // 2사분면
            let third = cutter(array, 0, div, div, div*2, div); // 3사분면
            let fourth = cutter(array, div, div*2, div, div*2, div); // 4사분면

            recur(first);
            recur(second);
            recur(third);
            recur(fourth);
        }
    }

    recur(arr)

    return answer;
}

console.log(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))