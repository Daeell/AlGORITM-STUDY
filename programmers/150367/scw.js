function solution(numbers) {
    var answer = [];

    temp : function find_node(arr){
        let mid = Math.ceil(arr.length/2);
        console.log(arr)
        if (arr[mid]===1){
            let arr1 = arr.slice(0, mid-1);
            let arr2 = arr.slice(mid,arr.length);
            find_node(arr1)
            find_node(arr2)
        } else {
            
        }
    }
    
    for(let i=0;i<numbers.length;i++){
        let temp = numbers[i].toString(2);
        if (temp.length%2 ===0){
            temp = '0'+temp
        }
        
    }

    return answer;
}

console.log(solution([63,111,95]))