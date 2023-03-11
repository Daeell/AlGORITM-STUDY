function solution(str1, str2) {
    var answer = 0;
    str1 = str1.toLowerCase();
    str2 = str2.toLowerCase();
    var str1_arr = [];
    var str2_arr = [];
    var union = [];
    var intersection = 0;

    for(let i=0; i<str1.length-1;i++){
        let temp = str1.slice(i,i+2);
        if (temp.length===2){
            if(/^[a-zA-Z]+$/.test(temp)){
                str1_arr.push(temp)
            }
        }
    }

    for(let i=0; i<str2.length-1;i++){
        let temp = str2.slice(i,i+2);
        if (temp.length===2){
            if(/^[a-zA-Z]+$/.test(temp)){
                str2_arr.push(temp)
            }
        }
    }

    for(let i=0;i<str1_arr.length;i++){
        for(let j=0;j<str2_arr.length;j++){
            if(str1_arr[i]===str2_arr[j]){
                intersection++;
                str2_arr[j] =-1;
                str1_arr[i] =-1;
                break;
            }
        }
    }

    union = str1_arr.length + str2_arr.length - intersection;

    if(union ===0 && intersection===0){
        answer = 65536
    } else{
        answer = parseInt((intersection/union)*65536)
    }

    return answer;
}

// 다른 사람 풀이
// function solution (str1, str2) {

//     function explode(text) {
//       const result = [];
//       for (let i = 0; i < text.length - 1; i++) {
//         const node = text.substr(i, 2);
//         if (node.match(/[A-Za-z]{2}/)) {
//           result.push(node.toLowerCase());
//         }
//       }
//       return result;
//     }
  
//     const arr1 = explode(str1);
//     const arr2 = explode(str2);
//     const set = new Set([...arr1, ...arr2]);
//     console.log(set)
//     let union = 0;
//     let intersection = 0;
  
//     set.forEach(item => {
//       const has1 = arr1.filter(x => x === item).length;
//       const has2 = arr2.filter(x => x === item).length;
//       union += Math.max(has1, has2);
//       intersection += Math.min(has1, has2);
//     })
//     return union === 0 ? 65536 : Math.floor(intersection / union * 65536);
//   }

console.log(solution("FRANCE", "french"))