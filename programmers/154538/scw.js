function solution(x, y, n) {

    if(x===y) return 0;
    var answer = 0;
    const dp = Array(y+1).fill(Infinity);
    dp[x] = 0;

    for(let i=x+1; i<y+1;i++){
        if(x<= i-n) dp[i] = Math.min(dp[i], dp[i-n]+1);
        if(i%2===0 && x<= i/2) dp[i] = Math.min(dp[i], dp[i/2]+1);
        if(i%3===0 && x<= i/3) dp[i] = Math.min(dp[i], dp[i/3]+1);
    }

    
    answer = dp[y]===Infinity ? -1 : dp[y];

    return answer;
}

console.log(solution(10, 40, 5))

// 5 7 9 10 11 12 시간초과
// function solution(x, y, n) {
//     var answer = -1;
//     var arr =[[x, 0]];

//     if(x===y){
//         return 0;
//     }
//     let idx=0
//     check_ : while (arr.length>0){
//         if(idx >=arr.length){
//             break;
//         }
        
//         let [temp, cnt] = arr[idx];

//         for(let i=0;i<3;i++){
//             let temp2=0;
//             if(i===0){
//                 temp2 = temp + n
//             } else if(i===1){
//                 temp2 = temp*2
//             } else{
//                 temp2 = temp*3
//             }
    
//             if(temp2<y){
//                 arr.push([temp2, cnt+1])
//             } else if (temp2 === y ){
//                 answer = cnt+1;
//                 break check_;
//             }
//         }
//         idx++;
//     }
    
//     return answer;
// }