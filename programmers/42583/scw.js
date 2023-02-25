function solution(bridge_length, weight, truck_weights) {
    var answer = 0; // 전체 걸린 시간

    var bridge_status = Array.from({length: bridge_length}, () =>0); // bridge length 만큼 공간을 만들어줌 (1초에 한칸씩 움직일거야)

    var bridge_sum = 0;
    
    answer++; // 1초를 올림
    bridge_status.shift(); // 1초가 지났으니깐 앞에 있는게 나가고 뒤에 하나 들어올거야
    bridge_sum += truck_weights[0]; // 다리 위에 무게를 올려줌
    bridge_status.push(truck_weights.shift()); // 1초 때 truck 제일 앞칸에 있는게 하나 들어오고
    
    while(bridge_sum > 0){ // 다리 위에 무게가 남아있다는건 다리를 지나는 트럭이 있다는거
        answer++; // 1초 올리고
        bridge_sum -= bridge_status.shift(); // 제일 앞에 있는걸 빼줌 -- 도착한 트럭

        if(truck_weights.length>0 && bridge_sum + truck_weights[0] <= weight){ // 트럭이 남아있고 && 다리 위 무게와 트럭 리스트 첫칸의 무게가 다리가 견딜 수 있는 무게보다 작다면
            bridge_sum += truck_weights[0]; // 다리 위에 무게를 추가해주고
            bridge_status.push(truck_weights.shift()); // 다리위에 트럭을 추가해주고
        } else {
            bridge_status.push(0); // 위 if문에 안걸리면 시간만 흘려서 보내야하니깐 0을 추가해줌
        }
    }

    return answer;
}

console.log(solution(2, 10, [7,4,5,6]))

