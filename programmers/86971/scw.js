function solution(n, wires) {
    var answer = [];
    var graph = {};

    for (let i=0;i<wires.length;i++){
        const [w1, w2] = wires[i];
        if(!graph[w1]){
            graph[w1] = [w2];
        } else if(graph[w1]){
            graph[w1].push(w2);
        }
        if(!graph[w2]){
            graph[w2] = [w1];
        } else if(graph[w2]){
            graph[w2].push(w1);
        }
        
    }

    for(let wire of wires){
        const [s, e] = wire;
        const graph_copy = [...graph[s]]; // 시작점과 연결된 노드들을 복사
        const visited = {};
        let cnt = 1; // s부터 시작이니깐 1개

        visited[s] = true; // 이미 방문한 곳은 true로 바꿈 -- 즉 s와 e는 이미 방문했다 == 끊어짐
        visited[e] = true;

        while (graph_copy.length>0){
            let tmp = graph_copy.pop(); // 하나씩 빼면서 연결된 부분을 찾는다
            if(!visited[tmp]){ // 아직 방문하지 않았으면
                visited[tmp] = true; // 방문처리하고
                graph_copy.push(...graph[tmp]); // 해당 노드와 연결된 애들을 또 복사해서 넣어줌
                cnt++;
            }
        }
        answer.push(Math.abs(cnt*2-n));
    }

    return Math.min(...answer);
}

console.log(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))