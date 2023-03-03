function solution(numbers) {
    var answer = [];

    for (let i=0;i<numbers.length;i++){
        
        if(numbers[i]%2 === 0){
            answer.push(numbers[i]+1)
        } else {
            let bi_num = numbers[i].toString(2);
            bi_num = '0'+bi_num;
            bi_num = [...bi_num]
            for (let i = bi_num.length-1; i>=0;i--){
                if(bi_num[i]==='0'){
                    bi_num[i]= '1';
                    bi_num[i+1] = '0';
                    break;
                }
            }
            bi_num = bi_num.join("");
            answer.push(parseInt(bi_num,2));
        }
        
    }
    
    return answer;
}

console.log(solution([2,7]))


// 시간초과 - 10, 11
// function solution(numbers) {
//     var answer = [];

//     for (let i=0;i<numbers.length;i++){
//         let bi_num = numbers[i].toString(2);
//         let cnt = numbers[i]+1;
        
//         while (true){
//             bi_cnt = cnt.toString(2);
//             if( bi_cnt.length < bi_num.length){
//                 bi_cnt = bi_cnt.padStart(bi_num.length,'0');
//             } else if (bi_cnt.length> bi_num.length){
//                 bi_num = bi_num.padStart(bi_cnt.length, '0')
//             }

//             let check_cnt=0;
//             for (let i=0; i<bi_num.length;i++){
//                 if(bi_num[i] !==bi_cnt[i]){
//                     check_cnt++;
//                 }
//             }

//             if(check_cnt<=2){
//                 answer.push(cnt)
//                 break;
//             }

//             cnt++;
//         }
//     }
    
//     return answer;
// }
