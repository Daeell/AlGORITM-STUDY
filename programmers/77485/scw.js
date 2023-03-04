function solution(rows, columns, queries) {
    var answer = [];
    const arr = Array.from(new Array(rows), ()=> new Array(columns).fill(0));
    var num=1;
    for(let i =0; i<rows;i++){
        for(let j =0;j<columns;j++){
            arr[i][j] = num;
            num++
        }
    }

    while (queries.length>0){
        let [x1, y1, x2, y2] = queries.shift();
        let temp = [];
        x1 = x1-1;
        y1 = y1-1;
        x2 = x2-1;
        y2 = y2-1;

        for(let i=y1; i<=y2;i++){
            temp.push(arr[x1][i])
        }

        for(let i=x1+1; i<=x2;i++){
            temp.push(arr[i][y2])
        }

        for(let i=y2-1; i>=y1;i--){
            temp.push(arr[x2][i])
        }

        for(let i=x2-1; i>x1;i--){
            temp.push(arr[i][y1])
        }

        answer.push(Math.min(...temp))

        let temp_for_rot = temp.pop();
        temp.unshift(temp_for_rot);

        for(let i=y1; i<=y2;i++){
            arr[x1][i] = temp.shift();
        }

        for(let i=x1+1; i<=x2;i++){
            arr[i][y2] = temp.shift();
        }

        for(let i=y2-1; i>=y1;i--){
            arr[x2][i] = temp.shift();
        }

        for(let i=x2-1; i>x1;i--){
            arr[i][y1] = temp.shift();
        }

    }

    return answer;
}

console.log(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))