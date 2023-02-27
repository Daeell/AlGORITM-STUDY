function solution(numbers){
    var answer= Array(numbers.length).fill(-1);
    var temp=[];

    for (let i=0;i<numbers.length;i++){
        while( temp.length >0 && numbers[temp.at(-1)] < numbers[i]){
            answer[temp.pop()] = numbers[i];
        }
        temp.push(i);
    }

    return answer;
}

console.log(solution([2, 3, 3, 5]))

// 시간초과
// function solution(numbers) {
//     var answer = [];

//     for(let i=0;i<numbers.length-1;i++){
//         for(let j=i+1;j<numbers.length;j++){
//             if(numbers[i]<numbers[j]){
//                 answer.push(numbers[j]);
//                 break;
//             } else if( j === numbers.length-1){
//                 answer.push(-1);
//             }
//         }
//     }
//     answer.push(-1);

//     return answer;
// }