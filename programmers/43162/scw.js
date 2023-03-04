function solution(n, computers) {
    var answer = 0;

    function dfs(y, x) {

        if (computers[y][x] === 1) {
            computers[y][x] = -1;
        }

        for (let j=0;j<n;j++){
            if(computers[y][j]===1){
                computers[y][j]=-1;
                computers[j][y]=-1;
                dfs(j,j)
            }
        }
    }

    for (let i = 0; i < n; i++) {
        if (computers[i][i] === 1) {
            answer++;
            dfs(i, i)
        }
    }

    return answer;
}

console.log(solution(2, [[1, 1],[1,1]]))
